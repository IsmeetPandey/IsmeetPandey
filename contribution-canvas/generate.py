#!/usr/bin/env python3
"""Generate a contribution-art SVG from canvas.json.

This project intentionally does not alter Git history or timestamps.
"""
from __future__ import annotations

import html
import json
from pathlib import Path

LEVELS = {
    "0": "#ebedf0",
    "1": "#9be9a8",
    "2": "#40c463",
    "3": "#30a14e",
    "4": "#216e39",
}
CELL = 14
GAP = 4
PAD = 18


def load_canvas(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("rows")
    if not isinstance(rows, list) or len(rows) != 7:
        raise ValueError("canvas.json must contain exactly 7 rows")
    if any(not isinstance(row, str) or len(row) != 52 for row in rows):
        raise ValueError("each row must be a 52-character string")
    if any(char not in LEVELS for row in rows for char in row):
        raise ValueError("rows may only contain digits 0-4")
    return rows


def build_svg(rows: list[str]) -> str:
    width = PAD * 2 + 52 * (CELL + GAP) - GAP
    height = PAD * 2 + 7 * (CELL + GAP) - GAP
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="Contribution canvas">'
    ]
    for y, row in enumerate(rows):
        for x, level in enumerate(row):
            px = PAD + x * (CELL + GAP)
            py = PAD + y * (CELL + GAP)
            parts.append(
                f'<rect x="{px}" y="{py}" width="{CELL}" height="{CELL}" rx="3" '
                f'fill="{html.escape(LEVELS[level])}"/>'
            )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    root = Path(__file__).resolve().parent
    rows = load_canvas(root / "canvas.json")
    output = root / "contribution-canvas.svg"
    output.write_text(build_svg(rows), encoding="utf-8")
    print(f"Generated {output.name}")


if __name__ == "__main__":
    main()
