# Book Generator

Makes illustrated 12-page picture books for the Nighttime Books reader
(`../nighttime-books`, the Android app for the Bigme HiBreak). Images come from
Nano Banana (`google/gemini-3.1-flash-image`) on OpenRouter, about $0.07 each.

## HTML front end (no server)

Open `index.html` in Chrome or Firefox (double-click, or `xdg-open index.html`).

1. Paste an OpenRouter key at the top (kept in this browser's localStorage).
2. **Load an example** (three come with finished pictures: farm, kittens, r01-sit-pip),
   **New book**, or **Import book JSON** with any of `books/*.json`.
3. Edit title, style, palette, character and the page text and image beats.
4. **Generate missing**: character sheet(s) first, then cover and pages, which get the sheet(s) as references.
   Click an image to see its prompt; **Redo** regenerates one page.
5. **Download device zip** (or **Write to folder…** in Chrome), unzip into `out/`, then
   `../nighttime-books/push.sh <slug>`.

Bedtime books use one main character and one reference sheet. Reading books have a named cast;
each page only gets the references for the names in its text or beat, and the cast sheets are
shared by every reading book in the browser. Existing raw images (`work/<slug>/raw/*.png`,
`work/reading/cast/*.png`) can be loaded with **Import images…**.

Books and images live in the browser's IndexedDB. Use **Export project file** to back one up.

## Python pipeline (the original)

    python3 plan2json.py                 # books-plan.md   -> books/*.json
    python3 reading2json.py              # reading-plan.md -> books/r01-*.json (+ vocabulary check)
    python3 gen.py build <slug> [--only char,0,3] [--force]
    python3 gen.py cast                  # reading-set reference sheets
    python3 gen.py package <slug>        # out/<slug> + work/<slug>/contact.png

The key comes from `OPENROUTER_API_KEY` or `../openrouter.token`.

## Image sizes

Device pages are WebP at quality 85, about 50 KB each (0.5–3 MB a book). The model returns PNG,
and even these flat-looking pictures have ~40,000 colours from soft edges and grain, so a lossless
page is 0.7–1 MB. `work/` (the model's originals) and `out/` are not in git; `examples/` holds three
finished books as WebP for the web page.
