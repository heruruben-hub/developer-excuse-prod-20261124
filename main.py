#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

import os

ENTRY = "It passed all 400 tests. The bug was in test 401 \u2014 the one we call production."

assert "\n" not in ENTRY
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
