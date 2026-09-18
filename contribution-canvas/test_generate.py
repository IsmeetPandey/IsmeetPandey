import tempfile
import unittest
from pathlib import Path

import generate


class GenerateTests(unittest.TestCase):
    def test_canvas_shape(self):
        rows = generate.load_canvas(Path("canvas.json"))
        self.assertEqual(len(rows), 7)
        self.assertTrue(all(len(row) == 52 for row in rows))

    def test_svg_contains_all_cells(self):
        rows = generate.load_canvas(Path("canvas.json"))
        self.assertEqual(generate.build_svg(rows).count("<rect "), 52 * 7)

    def test_invalid_canvas_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text('{"rows":["0" * 51]}', encoding="utf-8")
            with self.assertRaises(ValueError):
                generate.load_canvas(path)


if __name__ == "__main__":
    unittest.main()
