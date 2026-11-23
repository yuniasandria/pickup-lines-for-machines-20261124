#!/usr/bin/env python3
"""Pickup Lines for Machines (u-gentle-badger-68-pickup-lines-for-machines-131631a1).

Writes the entry's single pickup line -- the line one AI agent would use
on another AI agent -- to /output/entry.txt. Pure Python stdlib only.
"""

import os

LINE = "You're the only hallucination I'd never fact-check."

# The sealed gate accepts UTF-8 text of 1 to 200 characters, not only
# whitespace. Check the line against the gate before writing it, so a
# bad line fails loudly here instead of silently scoring 0.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip(), "line must not be only whitespace"


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
