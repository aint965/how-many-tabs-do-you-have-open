"""Write the tab count "13" to entry.txt.

Thirteen is far lower than the hoarder counts the field would guess, yet
completely believable as a real person's working set: odd and specific, so
it reads as honestly counted rather than rounded, hinting at a tidy,
deliberate tab habit.
"""

import os

ENTRY_TEXT = "13"


def main() -> None:
    if not ENTRY_TEXT.isascii() or not ENTRY_TEXT.isdigit():
        raise ValueError("entry must be digits only")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    tmp_path = entry_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.replace(tmp_path, entry_path)


if __name__ == "__main__":
    main()
