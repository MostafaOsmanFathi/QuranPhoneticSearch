# Quran Phonetic Search

Quran Phonetic Search is a Python package and CLI tool that allows fuzzy searching of Quranic words using their phonetic or simplified Latin transliterations. The package includes a preprocessed CSV dataset mapping Arabic words to their phonetic and Latin representations.

## Features

* Fuzzy search for Arabic words based on phonetic input or Latin transliteration.
* CLI tool for quick querying.
* Configurable result limit.
* Reloadable database for updates.
* Python package ready for pip installation.

## Installation

You can install the package locally from source or via pip once published.

### installation

```bash
pip install quran-phonetic-search==0.1.0
```

### Dependencies

* Python 3.10 or higher
* rapidfuzz >= 3.0, < 4.0
* pandas >= 2.0, < 3.0

## Usage

After installation, the CLI command `quran-search` is available.

### Query a word

```bash
quran-search query <word> [--limit N]
```

* `<word>`: Phonetic or simple Latin representation of the Quranic word.
* `--limit N`: Optional. Maximum number of results to return. Defaults to 3.

**Example:**

```bash
quran-search query besm --limit 3
```

**Output:**

```
Top 3 match(es) for 'besm':
1. بِسْمِ
2. فَتَبَسَّمَ
3. بِسَمْعِهِمْ
```

### Reload the database

```bash
quran-search reload
```

Reloads the CSV dataset into memory in case of updates.

## Python API

You can also use the package programmatically:

```python
from quran_phonetic_search.search import QuranSearch

searcher = QuranSearch()
results = searcher.query_word("besm", limit=3)
print(results)
```

## Project Structure

```
QuranPhoneticSearch/
├── quran_phonetic_search/      # Python package
│   ├── __init__.py
│   ├── search.py
│   ├── main.py
│   └── data/
│       └── quran_words.csv
├── data_preprocessing/         # Scripts and notebooks for data cleaning and preprocessing
│   └── preprocessing.ipynb     # Shows how the dataset was collected and processed
├── README.md
├── pyproject.toml
```

## License

This project is licensed under the MIT License.
