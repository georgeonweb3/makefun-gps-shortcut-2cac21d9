"""GPS excuse entry: the bridge closed in 2019.

Writes the one-line GPS excuse to /output/entry.txt as UTF-8,
with no trailing newline.
"""

import os

ENTRY = "The bridge closed in 2019 and nobody told the map, so I sent you across it anyway — I take no blame; the river sends its regards."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
