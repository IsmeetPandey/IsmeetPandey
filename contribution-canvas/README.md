# 🧩 Contribution Canvas

A tiny, dependency-free GitHub contribution-art experiment.

The generator creates a clean SVG from a 52×7 canvas pattern. It is deliberately honest: it never rewrites Git history, changes author dates, or creates fake commits.

## Run

```bash
python generate.py
python -m unittest test_generate.py
```

The output is `contribution-canvas.svg`.

## Why this exists

Contribution graphs are a record of real GitHub activity. This project explores the visual side without changing that history.

Edit `canvas.json` to experiment with new patterns, then make genuine code/docs/test changes as the project evolves.
