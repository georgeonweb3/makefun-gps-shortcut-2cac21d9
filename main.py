#!/usr/bin/env python3
"""Entry for make.fun 'The GPS Swears It Was a Shortcut'.

Writes the GPS's one-line excuse to /output/entry.txt (no trailing
newline) and prints it. The line is the blind-tournament winner:
a closed bridge, a stale map, and a river that sends its regards.
"""
import os

LINE = (
    "The bridge closed in 2019 and nobody told the map, so I sent you "
    "across it anyway \u2014 I take no blame; the river sends its regards."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
