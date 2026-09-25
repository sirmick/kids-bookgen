#!/usr/bin/env python3
"""Parse reading-plan.md into books/r01-*.json … and print the cumulative vocabulary check."""
import re, json, os, pathlib, sys
src = pathlib.Path(__file__).with_name("reading-plan.md").read_text()
head = src.split("\n---\n", 1)[0]
style = re.search(r"## Shared style sheet.*?\n\n(.*?)\n\n", head, re.S).group(1).replace("\n", " ").strip()
palette = re.search(r"\*\*Palette:\*\*\s*(.+)", head).group(1).strip()
reference = re.search(r"\*\*Reference:\*\*\s*(\S+)", head).group(1)
CAST = {  # name -> description used in prompts
    "Pip": "Pip, a small brown-and-white beagle puppy with floppy ears and a red collar",
    "Tip": "Tip, a small ginger kitten with white paws and big round eyes",
    "Mim": "Mim, a small grey tabby kitten with dark stripes, white paws and green eyes",
    "Sam": "Sam, a very big shaggy grey-and-white old English sheepdog with hair over his eyes",
    "Bob": "Bob, a stocky wrinkly tan bulldog with a black nose",
    "Chip": "Chip, a tiny tan chihuahua with huge ears",
    "Spot": "Spot, a white dalmatian with black spots",
    "Jack": "Jack, a small white jack russell terrier with a brown patch over one eye",
    "Max": "Max, a fawn pug with a black face and curly tail",
    "Zip": "Zip, a slim grey greyhound with a long nose",
}
os.chdir(pathlib.Path(__file__).resolve().parent)
os.makedirs("books", exist_ok=True)
known = set(); ok = True; slugs = []
for sec in re.split(r"\n## (?=\d+\. )", src.split("\n---\n", 1)[1])[1:]:
    h, body = sec.split("\n", 1)
    num, title = re.match(r"(\d+)\. (.+)", h).groups()
    sight = re.search(r"\*\*Sight words:\*\*\s*(.+)", body).group(1)
    sight = [] if sight.strip() == "none" else [w.strip() for w in sight.split(",")]
    pages = []
    names = set()
    for n, word, text, beat in re.findall(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", body, re.M):
        pages.append({"n": int(n), "word": word.strip(), "text": text.strip(), "beat": beat.strip(), "text_pos": "bottom"})
        if word.strip() and word.strip()[0].isupper(): names.add(word.strip())
    # vocabulary check: every token must already be known or introduced on this page or earlier in the book
    known |= {w.lower() for w in sight}
    for p in pages:
        if p["word"]: known.add(p["word"].lower())
        for tok in re.findall(r"[A-Za-z']+", p["text"]):
            if tok.lower() not in known:
                ok = False; print(f"  VOCAB: book {num} page {p['n']}: '{tok}' not taught yet  ({p['text']})")
    slug = f"r{int(num):02d}-" + re.sub(r"[^a-z]+", "-", title.lower()).strip("-")
    cast_here = [m for m in CAST if re.search(r"\b" + m + r"\b", " ".join(p["text"] + " " + p["beat"] for p in pages))]
    character = " ".join(CAST[m] + "." for m in cast_here)
    book = {"slug": slug, "title": title, "character": character, "cast": cast_here, "refrain": "",
            "palette": palette, "sky": "plain cream or pale sky background, no scenery",
            "cover": f"{pages[0]['beat']} Big, simple and friendly.", "style": style,
            "reference": reference, "pages": pages}
    assert len(pages) == 12, (slug, len(pages))
    json.dump(book, open(f"books/{slug}.json", "w"), indent=1, ensure_ascii=False)
    slugs.append(slug)
    print(f"{slug}: {len([p for p in pages if p['word']])} new words, cast {cast_here}")
print("vocabulary check:", "OK" if ok else "FAILED"); print("total words taught:", len(known))
sys.exit(0 if ok else 1)
