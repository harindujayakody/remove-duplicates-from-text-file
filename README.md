# Remove-Duplicates-from-Text-File
This Python program reads a text file, removes duplicate lines, and saves the cleaned content to a new file. It also provides a summary of how many duplicates were found and how many unique lines were kept. The unique lines are sorted in ascending order before being saved to the new file.

## Features
- Removes duplicate lines from a text file.
- Outputs a clean version of the file with unique lines sorted in ascending order.
- Displays a summary of the number of duplicate and unique lines in the terminal.
- Clears the terminal screen before displaying the output for a clean experience.

## Usage
Running the Script
Ensure your input file (e.g., input.txt) is in the same directory as the script.
By default the cleaned content is saved to a new file called new.txt.

Execute the Python script with:
python main.py

Pass a different input file, or choose the output file with `-o`:

```bash
python main.py my-file.txt
python main.py my-file.txt -o cleaned.txt
python main.py --help
```

If the input file does not exist, the script prints an error and exits instead of crashing.

## Installation

To use the script, follow these steps:

1. Clone the repository or download the script.
2. Make sure you have Python 3 installed on your system.

```bash
git clone https://github.com/harindujayakody/remove-duplicates-from-text-file.git
cd remove-duplicates-from-text-file
python main.py
```

## License

This project is licensed under the GNU General Public License v3.0 — see the LICENSE file for details.
