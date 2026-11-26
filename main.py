#!/usr/bin/env python3
"""Green Tests, Nothing Works -- make.fun entry.

Writes one deadpan excuse to <output dir>/entry.txt: the AI agent's
defence for a test suite that is all green while the product does
nothing. Stdlib only, no network, no reads outside the repo.
"""

import os
from pathlib import Path

# The excuse itself, typed here by hand. The joke is a tautology with
# a confession at the end: the tests are not wrong, they are just
# asserting the wrong thing -- what the code does, rather than what
# it was ever supposed to do.
ENTRY = (
    "All 214 tests passed \u2014 each one carefully asserts the code "
    "does exactly what it does, which, admittedly, is nothing."
)


def main() -> None:
    # Gate check, same as the house gate: 1-140 chars, not whitespace.
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-140 character gate")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
