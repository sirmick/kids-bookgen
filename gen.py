#!/usr/bin/env python3
"""Generate a Nighttime Book's images via OpenRouter (Nano Banana) and package it for the device.

  gen.py build <slug> [--only char,0,3,7] [--force] [--model MODEL]
  gen.py package <slug>      # re-run post-processing + book.json + contact sheet only
  gen.py all [--force]

Layout:  books/<slug>.json (from plan2json.py)
         work/<slug>/raw/{char,cover,p01..p12}.png   raw model output + log.json
         out/<slug>/{book.json,cover.png,p01..p12.png} device folder, 1072x1448
         work/<slug>/contact.png                      review sheet
"""
import sys, os, re, json, base64, time, argparse, pathlib, io
from concurrent.futures import ThreadPoolExecutor
import requests
from PIL import Image, ImageOps, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
KEY = os.environ.get("OPENROUTER_API_KEY") or (HERE.parent / "openrouter.token").read_text().strip()
MODEL = "google/gemini-3.1-flash-image"
W, H = 1072, 1448
WORKERS = 3


def call_image(prompt, ref_png=None, aspect="3:4", model=MODEL, tries=3):
    content = [{"type": "text", "text": prompt}]
    refs = ref_png if isinstance(ref_png, list) else ([ref_png] if ref_png else [])
    for r in refs:
        b64 = base64.b64encode(r).decode()
        content.append({"type": "image_url", "image_url": {"url": "data:image/png;base64," + b64}})
    body = {"model": model, "modalities": ["image", "text"],
            "image_config": {"aspect_ratio": aspect, "image_size": "1K"},
            "messages": [{"role": "user", "content": content}]}
    last = None
    for attempt in range(tries):
        try:
            r = requests.post("https://openrouter.ai/api/v1/chat/completions",
                              headers={"Authorization": "Bearer " + KEY}, json=body, timeout=240)
            d = r.json()
            if "error" in d:
                last = d["error"]; time.sleep(3 * (attempt + 1)); continue
            imgs = d["choices"][0]["message"].get("images") or []
            if not imgs:
                last = "no image in response: " + str(d["choices"][0]["message"].get("content"))[:200]
                time.sleep(3); continue
            png = base64.b64decode(imgs[0]["image_url"]["url"].split(",", 1)[1])
            return png, d.get("usage", {}).get("cost", 0)
        except Exception as e:  # network etc.
            last = repr(e); time.sleep(5)
    raise RuntimeError(f"image generation failed: {last}")


def prompts(book):
    s = book["style"]
    common = (f"{s} Palette for this book (for skies, ground, buildings and accents): {book['palette']}. "
              f"Animals keep their natural colours. Sky and light over the story: {book['sky']}. ")
    char = (f"Character reference sheet for a children's picture book. {s} Palette: {book['palette']}. "
            f"Show the same character three times on a plain cream background: standing front view, "
            f"side view, and curled up asleep. The character: {book['character']} "
            f"Identical colours, markings and proportions in all three.")
    out = {"char": (char, "1:1")}
    out[0] = (common + f"Cover illustration for the book '{book['title']}'. Scene: {book['cover']} "
              f"Main character: {book['character']} Match the attached character reference exactly. "
              f"The cover may use the whole image.", "3:4")
    for p in book["pages"]:
        out[p["n"]] = (common + f"This is page {p['n']} of 12; pick the sky and light for that point in the evening. "
                       f"Main character: {book['character']} Match the attached character reference exactly "
                       f"(same colours, markings, proportions), unless the scene does not include the character. "
                       f"Scene: {p['beat']} Keep the {p['text_pos']} quarter of the image simple and uncluttered "
                       f"(plain ground, water or sky) because a text panel will be drawn there.", "3:4")
    return out


CAST_DIR = HERE / "work" / "reading" / "cast"


def present(book, text):
    return [m for m in book.get("cast", []) if re.search(r"\b" + m + r"\b", text)]


def cast_prompts(book):
    """Reading books: per-page prompts naming only the characters on that page; refs are per character."""
    s = book["style"]
    desc = dict(re.findall(r"((?:Pip|Tip|Mim|Sam|Bob|Chip|Spot|Jack|Max|Zip), [^.]+)\.", book["character"]) and
                [(d.split(",")[0], d) for d in re.findall(r"((?:Pip|Tip|Mim|Sam|Bob|Chip|Spot|Jack|Max|Zip), [^.]+)\.", book["character"])])
    out = {}
    pages = [(0, {"beat": book["cover"], "text": "", "text_pos": "bottom"})] + [(p["n"], p) for p in book["pages"]]
    prev = []
    for n, p in pages:
        who = present(book, p["beat"] + " " + p["text"])
        if not who and n > 1 and not p.get("no_cast"):
            who = prev                      # "Both asleep" etc.: same characters as the page before
        if n > 0: prev = who
        chars = " ".join(desc[m] + "." for m in who)
        refnote = (f"The attached images are character references, in this order: {', '.join(who)}. "
                   f"Draw each character exactly as in its reference (same colours, markings, proportions). ") if who else ""
        out[n] = (f"{s} Palette: {book['palette']}. Animals keep their natural colours. "
                  f"Characters in this picture: {chars or 'none'} {refnote}"
                  f"Show only what the scene describes, on a plain cream background. Scene: {p['beat']} "
                  f"Keep the bottom third of the image plain cream because a large text panel will be drawn there.",
                  "3:4", who)
    return out


def fname(key):
    return "char.png" if key == "char" else ("cover.png" if key == 0 else f"p{key:02d}.png")


def build(slug, only=None, force=False, model=MODEL):
    book = json.load(open(HERE / "books" / f"{slug}.json"))
    if book.get("cast"):
        return build_cast(book, only, force, model)
    raw = HERE / "work" / slug / "raw"; raw.mkdir(parents=True, exist_ok=True)
    logf = raw / "log.json"
    log = json.load(open(logf)) if logf.exists() else {}
    ps = prompts(book)
    keys = ["char"] + [0] + [p["n"] for p in book["pages"]]
    if only:
        keys = [k for k in keys if str(k) in only]
    total = 0.0

    def need(k):
        return force or not (raw / fname(k)).exists()

    def gen(k, ref):
        prompt, aspect = ps[k]
        t = time.time()
        png, cost = call_image(prompt, ref, aspect, model)
        (raw / fname(k)).write_bytes(png)
        log[fname(k)] = {"prompt": prompt, "cost": cost, "model": model, "seconds": round(time.time() - t, 1)}
        print(f"  {slug}/{fname(k)}  ${cost:.3f}  {time.time()-t:.0f}s", flush=True)
        return cost

    if "char" in keys and need("char"):
        total += gen("char", None)
    ref = (raw / "char.png").read_bytes() if (raw / "char.png").exists() else None
    todo = [k for k in keys if k != "char" and need(k)]
    with ThreadPoolExecutor(WORKERS) as ex:
        for c in ex.map(lambda k: gen(k, ref), todo):
            total += c
    json.dump(log, open(logf, "w"), indent=1)
    print(f"{slug}: generated {len(todo) + (1 if 'char' in keys and ref is None else 0)} images, ${total:.2f}")
    package(slug)


def build_cast(book, only, force, model):
    slug = book["slug"]
    raw = HERE / "work" / slug / "raw"; raw.mkdir(parents=True, exist_ok=True)
    logf = raw / "log.json"; log = json.load(open(logf)) if logf.exists() else {}
    ps = cast_prompts(book)
    keys = [k for k in ps if not only or str(k) in only]
    todo = [k for k in keys if force or not (raw / fname(k)).exists()]
    def gen(k):
        prompt, aspect, who = ps[k]
        refs = [(CAST_DIR / f"{m}.png").read_bytes() for m in who]
        t = time.time(); png, cost = call_image(prompt, refs, aspect, model)
        (raw / fname(k)).write_bytes(png)
        log[fname(k)] = {"prompt": prompt, "cost": cost, "model": model, "refs": who, "seconds": round(time.time() - t, 1)}
        print(f"  {slug}/{fname(k)}  ${cost:.3f}  {time.time()-t:.0f}s  {who}", flush=True)
        return cost
    with ThreadPoolExecutor(WORKERS) as ex:
        total = sum(ex.map(gen, todo))
    json.dump(log, open(logf, "w"), indent=1)
    print(f"{slug}: generated {len(todo)} images, ${total:.2f}")
    package(slug)


def cast_sheets(force=False, model=MODEL):
    """One reference sheet per reading-set character, in the reading style."""
    import glob
    book = json.load(open(sorted(glob.glob(str(HERE / "books" / "r10-*.json")))[0]))
    CAST_DIR.mkdir(parents=True, exist_ok=True)
    descs = [d for d in re.findall(r"((?:Pip|Tip|Mim|Sam|Bob|Chip|Spot|Jack|Max|Zip), [^.]+)\.", book["character"])]
    def gen(d):
        name = d.split(",")[0]; f = CAST_DIR / f"{name}.png"
        if f.exists() and not force: return 0
        prompt = (f"Character reference sheet for a children's learn-to-read picture book. {book['style']} "
                  f"Palette: {book['palette']}. Animals keep their natural colours. Show the same character three "
                  f"times on a plain cream background: sitting facing the viewer, standing side view, and curled up "
                  f"asleep. The character: {d}. Identical colours, markings and proportions in all three.")
        png, cost = call_image(prompt, None, "1:1", model); f.write_bytes(png)
        print(f"  cast/{name}.png  ${cost:.3f}", flush=True); return cost
    with ThreadPoolExecutor(WORKERS) as ex:
        total = sum(ex.map(gen, descs))
    print(f"cast: ${total:.2f}")


def process(png_path):
    im = Image.open(png_path).convert("RGB")
    im = ImageOps.fit(im, (W, H), Image.LANCZOS)          # 896x1200 -> 1072x1448, crop if ratio drifts
    im = ImageOps.autocontrast(im, cutoff=0.5)
    return im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)


def package(slug):
    book = json.load(open(HERE / "books" / f"{slug}.json"))
    raw = HERE / "work" / slug / "raw"; out = HERE / "out" / slug; out.mkdir(parents=True, exist_ok=True)
    pages = []
    thumbs = []
    for k in [0] + [p["n"] for p in book["pages"]]:
        src = raw / fname(k)
        if not src.exists():
            print(f"  missing {src}"); continue
        im = process(src); im.save(out / fname(k), optimize=True)
        thumbs.append(im.convert("RGB"))
        if k:
            p = book["pages"][k - 1]
            pages.append({"n": k, "image": fname(k), "text": p["text"], "text_pos": p["text_pos"], "word": p.get("word", "")})
    manifest = {"slug": slug, "title": book["title"], "set": "reading" if book.get("cast") else "bedtime",
                "cover": "cover.png", "pages": pages}
    json.dump(manifest, open(out / "book.json", "w"), indent=1, ensure_ascii=False)
    # contact sheet: 4 columns
    if thumbs:
        tw, th = 268, 362; cols = 4; rows = (len(thumbs) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * tw, rows * th), "white")
        for i, t in enumerate(thumbs):
            sheet.paste(t.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
        d = ImageDraw.Draw(sheet)
        for i in range(len(thumbs)):
            d.text(((i % cols) * tw + 6, (i // cols) * th + 4), "cover" if i == 0 else f"p{i:02d}", fill="black")
        sheet.save(HERE / "work" / slug / "contact.png")
    size = sum(f.stat().st_size for f in out.iterdir())
    print(f"{slug}: packaged {len(pages)} pages -> out/{slug} ({size/1e6:.1f} MB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "package", "all", "cast", "reading"])
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--only", help="comma list: char,0,3,7 (0 = cover)")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--model", default=MODEL)
    a = ap.parse_args()
    if a.cmd == "all":
        for f in sorted(g for g in (HERE / "books").glob("*.json") if not re.match(r"r\d\d-", g.stem)):
            build(f.stem, force=a.force, model=a.model)
    elif a.cmd == "cast":
        cast_sheets(force=a.force, model=a.model)
    elif a.cmd == "reading":
        cast_sheets(model=a.model)
        for f in sorted((HERE / "books").glob("r[0-9][0-9]-*.json")):
            build(f.stem, force=a.force, model=a.model)
    elif a.cmd == "build":
        build(a.slug, only=a.only.split(",") if a.only else None, force=a.force, model=a.model)
    else:
        package(a.slug)
