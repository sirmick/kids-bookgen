#!/bin/bash
# push.sh <slug>...   copies ../out/<slug> into the app's internal books folder on the HiBreak.
# Goes via /data/local/tmp and `run-as`, which needs the debug (debuggable) build of the app.
S=${ADB_SERIAL:-B6CLR0W2GEHB006000181}
PKG=com.mick.nighttimebooks
cd "$(dirname "$0")/.."   # books are built in the repo root
for slug in "$@"; do
  adb -s $S shell rm -rf /data/local/tmp/nb/$slug
  adb -s $S push out/$slug /data/local/tmp/nb/ >/dev/null
  adb -s $S shell "run-as $PKG sh -c 'mkdir -p files/books/$slug && rm -f files/books/$slug/* && cp /data/local/tmp/nb/$slug/* files/books/$slug/'"
  echo "$slug: $(adb -s $S shell run-as $PKG ls files/books/$slug | wc -l) files"
  adb -s $S shell rm -rf /data/local/tmp/nb/$slug
done
