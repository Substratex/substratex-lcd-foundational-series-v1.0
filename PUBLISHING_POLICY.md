# Publishing and Archival Policy

## 1. Published editions are immutable

Once a manuscript version has been publicly released, do not overwrite it. Corrections or substantive revisions should be published as a new version.

Examples:

- `v1.0` — first public edition
- `v1.1` — minor correction / clarification
- `v2.0` — substantive revision or architectural realignment

## 2. Preserve superseded editions

Superseded manuscripts remain part of the historical publication record. They may be marked obsolete or superseded, but should not be silently deleted.

## 3. Hash every release

Each public manuscript artifact should receive a SHA-256 checksum recorded under `provenance/hashes/` and in the release manifest.

Use `python tools/generate_hashes.py` after adding or replacing release artifacts.

## 4. Tag releases

Recommended Git tags:

- `series-v1.0`
- `paper-01-v1.0`
- `paper-02-v1.0`
- etc.

Annotated or signed tags are preferred when practical.

## 5. Record release metadata

Each release should record:

- paper number;
- title;
- version;
- publication date;
- canonical filename;
- SHA-256 hash;
- citation;
- DOI / external archive identifier if later assigned;
- supersedes / superseded-by relation;
- material changes from the previous edition.

## 6. Do not silently renumber the series

The canonical seven-paper order in `metadata/series-manifest.json` should remain stable. If future publications are added, append them or define a new series rather than retroactively changing historical numbering.

## 7. Manuscript-internal metadata

Before final publication, ensure the paper number, version, date, series name, rights notice, and citation inside each manuscript agree with the repository manifest.
