# Provenance Operations

This directory preserves release-level evidence for manuscript identity and publication chronology.

## Release procedure

1. Add the final manuscript files to the correct `papers/<paper>/` directory.
2. Confirm the manuscript title, paper number, version, and date match `metadata/series-manifest.json`.
3. Run:

   `python tools/generate_hashes.py`

4. Review `provenance/hashes/SHA256SUMS.txt`.
5. Copy `templates/release-manifest-template.md` into `provenance/releases/` and complete it.
6. Commit the manuscript, hashes, and release manifest together.
7. Create an annotated Git tag for the paper or series release.
8. If a DOI or external archive identifier is assigned later, add it without rewriting the released manuscript file.

Hashes demonstrate artifact identity and change detection. They do not establish source authenticity, scientific validity, or institutional certification.
