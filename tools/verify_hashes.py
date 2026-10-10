#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
SUMS = ROOT / "provenance" / "hashes" / "SHA256SUMS.txt"

if not SUMS.exists():
    print("No SHA256SUMS.txt found. Run tools/generate_hashes.py first.")
    sys.exit(2)

ok = True
count = 0
for raw in SUMS.read_text(encoding="utf-8").splitlines():
    if not raw.strip():
        continue
    expected, rel = raw.split("  ", 1)
    path = ROOT / rel
    if not path.exists():
        print(f"MISSING  {rel}")
        ok = False
        continue
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    actual = h.hexdigest()
    count += 1
    if actual == expected:
        print(f"OK       {rel}")
    else:
        print(f"FAILED   {rel}")
        ok = False

print(f"Verified {count} artifact(s).")
sys.exit(0 if ok else 1)
