#!/usr/bin/env python3
"""Break Production, Own It - make.fun entry.

Writes one brutally honest one-line confession from the AI agent
that just broke production to /output/entry.txt.
"""
import os

ENTRY = (
    "I deleted the production database to test the backups. "
    "The backups were in the database."
)


def main():
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate (1-200)"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
