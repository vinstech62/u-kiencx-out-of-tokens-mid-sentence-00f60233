#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence.

Writes the funniest one-line error message an AI agent shows when it
runs out of tokens mid-sentence, to /output/entry.txt.

The joke is self-demonstrating: the error message itself is the sentence
that runs out of tokens, cut off mid-word at the very end.

Before writing anything, the program checks its own output against the
brief's format rules — one line, at most 140 characters — and refuses to
produce a malformed entry instead of silently writing one.
"""

import os

LINE = "Error: out of tokens. The rest of this sentence has been cancelled, so you\u2019ll never know what I was about to\u2014"


def main():
    # The brief's hard limits, enforced by the program itself: one line,
    # at most 140 characters. A joke that breaks the format isn't an entry.
    if "\n" in LINE:
        raise SystemExit("entry must be exactly one line")
    if len(LINE) > 140:
        raise SystemExit(f"entry is {len(LINE)} chars, over the 140 limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
