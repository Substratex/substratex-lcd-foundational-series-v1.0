#!/usr/bin/env python3
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
OUT = ROOT / "provenance" / "hashes" / "SHA256SUMS.txt"

files = sorted(
    p for p in PAPERS.rglob("*")
    if p.is_file() and p.name not in {".gitkeep"} and not p.name.endswith("README.md")
)

lines = []
for path in files:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    rel = path.relative_to(ROOT).as_posix()
    lines.append(f"{h.hexdigest()}  {rel}")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
print(f"Wrote {len(lines)} hashes to {OUT}")
