#!/usr/bin/env python3
"""Copy finished books into examples/ for the web page and reader (WebP, prompts from log.json).

  make_examples.py farm kittens r01-sit-pip ...   add or refresh these books
  make_examples.py                                refresh every book already in examples/
"""
import sys, json, pathlib
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE / "examples"
IDX = ROOT / "index.json"


def save(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    Image.open(src).convert("RGB").save(dst, quality=85, method=6)


def main(slugs):
    idx = json.load(open(IDX)) if IDX.exists() else {"books": {}, "cast": {}}
    for slug in slugs or list(idx["books"]):
        book = json.load(open(HERE / "books" / f"{slug}.json"))
        raw = HERE / "work" / slug / "raw"
        log = json.load(open(raw / "log.json")) if (raw / "log.json").exists() else {}
        images = {}
        for f in sorted(raw.glob("*.png")):
            save(f, ROOT / slug / (f.stem + ".webp"))
            m = log.get(f.name, {})
            images[f.stem] = {k: m[k] for k in ("prompt", "cost", "model", "seconds", "refs") if m.get(k) is not None}
        missing = [k for k in ["cover"] + [f"p{p['n']:02d}" for p in book["pages"]] if k not in images]
        if missing:
            sys.exit(f"{slug}: missing raw images {missing}")
        idx["books"][slug] = {"title": book["title"], "images": images}
        for name in book.get("cast", []):
            save(HERE / "work" / "reading" / "cast" / f"{name}.png", ROOT / "cast" / f"{name}.webp")
            idx["cast"][name] = {}
        size = sum(f.stat().st_size for f in (ROOT / slug).iterdir())
        print(f"{slug}: {len(images)} images, {size / 1e6:.1f} MB")
    idx["books"] = dict(sorted(idx["books"].items()))
    json.dump(idx, open(IDX, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1:])
