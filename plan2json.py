#!/usr/bin/env python3
"""Parse books-plan.md into books/<slug>.json (one file per book). Idempotent."""
import re, json, os, pathlib
src = pathlib.Path(__file__).with_name("books-plan.md").read_text()
style = re.search(r"## Shared style sheet.*?\n\n(.*?)\n\n", src, re.S).group(1).replace("\n", " ").strip()
os.chdir(pathlib.Path(__file__).resolve().parent)
os.makedirs("books", exist_ok=True)
for sec in re.split(r"\n## (?=\d+\. )", src)[1:]:
    head, body = sec.split("\n", 1)
    num, title = re.match(r"(\d+)\. (.+)", head).groups()
    title = re.sub(r"\s*\(.*\)$", "", title).strip()
    def bullet(name):
        m = re.search(r"\*\*%s:\*\*\s*(.+)" % name, body); return m.group(1).strip() if m else ""
    pages = []
    for row in re.findall(r"^\| (\d+) \| (.+?) \| (.+?) \|$", body, re.M):
        n, text, beat = row
        pos = "top" if "[top]" in beat else "bottom"
        pages.append({"n": int(n), "text": text.strip(), "beat": beat.replace("[top]", "").strip(), "text_pos": pos})
    slug = {"1": "farm", "2": "zoo", "3": "reef", "4": "rainforest", "5": "savanna", "6": "woodland", "7": "fnq", "8": "cascades", "9": "garden", "10": "fireflies", "11": "kittens", "12": "dogs"}[num]
    book = {"slug": slug, "title": title, "character": bullet("Main character"), "refrain": bullet("Refrain"),
            "palette": bullet("Palette"), "sky": bullet("Sky arc") or bullet("Water arc"), "cover": bullet("Cover"),
            "style": bullet("Style") or style, "pages": pages}
    assert len(pages) == 12, (slug, len(pages))
    json.dump(book, open(f"books/{slug}.json", "w"), indent=1, ensure_ascii=False)
    print(slug, title, len(pages), "pages")
