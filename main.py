#!/usr/bin/env python3
"""One Word for the Boss: write the word to /output/entry.txt.

The word is "Seagull": the boss as a seagull manager -- swoops in,
squawks loudly, makes a mess of everything, and flies off before the
cleanup. One word, no caption, no explanation: it lands on its own.
"""

import os
import sys

WORD = "Seagull"


def check_word(word: str) -> None:
    """Refuse to write an entry the gate would reject.

    The sealed gate wants UTF-8 text of 1 to 30 characters, not only
    whitespace, and the judge only ever sees one word, so check all of
    that here instead of shipping an invalid file.
    """
    if not word or len(word) > 30 or not word.strip():
        raise SystemExit("word fails the 1-30 character gate")
    if any(ch.isspace() for ch in word):
        raise SystemExit("entry must be a single word, no spaces")


def main() -> int:
    check_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
