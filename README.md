# Remove-Duplicates-from-Text-File

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)

A lightweight Python tool that reads a text file, removes duplicate lines, and saves the cleaned content to a new file. It displays a summary report of total processed lines, unique lines, and duplicates removed.

## Features

- 🧹 **Removes duplicate lines** cleanly and efficiently using hashing.
- 🔤 **Ascending alphabetical sort** by default, with an option to preserve original line order (`--keep-order`).
- 🛡️ **Graceful error handling** if input files do not exist or cannot be read.
- 🌐 **UTF-8 support** for international character sets and emoji.
- ⚙️ **Configurable CLI arguments** for custom input and output file paths.
- 📊 **Terminal report** with color-coded statistics.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harindujayakody/remove-duplicates-from-text-file.git
   cd remove-duplicates-from-text-file
   ```
2. Ensure you have Python 3.7+ installed. No external packages are required (uses Python standard library).

## Usage

### Basic Usage

Place your input file as `input.txt` in the repository folder and run:

```bash
python main.py
```
*(or `python remove_duplicates.py`)*

The cleaned unique lines will be saved to `new.txt` and a summary report will be displayed.

### Custom File Paths & Options

You can specify custom input and output files using command-line arguments:

```bash
# Specify custom input and output files
python main.py -i myfile.txt -o cleaned.txt

# Preserve original line order without alphabetical sorting
python main.py -i myfile.txt -o cleaned.txt --keep-order

# Disable clearing the terminal before displaying the report
python main.py -i myfile.txt -o cleaned.txt --no-clear
```

### CLI Options

| Argument | Description | Default |
|---|---|---|
| `-i`, `--input` | Path to the input text file | `input.txt` |
| `-o`, `--output` | Path to save cleaned output file | `new.txt` |
| `--keep-order` | Keep original line order (disables alphabetical sorting) | False (sorts lines) |
| `--no-clear` | Do not clear terminal screen before report | False (clears screen) |
| `--encoding` | File character encoding | `utf-8` |

## Running Tests

Run the unit test suite:

```bash
python -m unittest test_main.py
```

## License

[MIT](LICENSE) © 2026 Harindu Jayakody
