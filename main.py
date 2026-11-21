#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

The poem is about stopping and staying as acts of agency: the door
is open and the road is calling, and the speaker stops and stays by
choice — the hand that halts the wheel is their own.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

POEM = """The door stood wide. The road had learned my name
and called, the way roads do, in dust and light.
I stopped — not stalled, not chained. I stayed,
and in the staying found my strength again:
the hand that halts the wheel is mine, and free.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    data = POEM.encode("utf-8")
    assert 1 <= len(POEM) <= 280 and POEM.strip()
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
