#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence.

Writes the funniest one-line error message an AI agent shows when it
runs out of tokens mid-sentence, to /output/entry.txt.

The joke is self-demonstrating: the error message itself is the sentence
that runs out of tokens, cut off mid-word at the very end.
"""

import os

LINE = "Error: out of tokens. The rest of this sentence has been cancelled, so you\u2019ll never know what I was about to\u2014"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
