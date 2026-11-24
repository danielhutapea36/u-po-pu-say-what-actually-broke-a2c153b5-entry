#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of honest, funny error copy to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only.
"""

import os
import sys

# The line: names the real failure (an upload lost in a mess of
# "final" folders), says what to do next (upload it again), and admits
# the system is just as lost as the user. 106 characters, one line.
ENTRY = "Your file is lost in a folder called final_final_v2_REAL. We can't find it either. Please upload it again."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Reject anything the gate would refuse, before writing."""
    if not line:
        raise ValueError("entry is empty")
    if line.strip() == "":
        raise ValueError("entry is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")


def main() -> int:
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)  # no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
