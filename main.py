import argparse
import os
import sys

def clear_terminal():
    # Clear the terminal screen
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

def remove_duplicates(input_file, output_file, sort_lines=True, encoding='utf-8'):
    """
    Remove duplicate lines from input_file and save unique lines to output_file.

    Returns:
        tuple: (duplicate_count, unique_count)
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    with open(input_file, 'r', encoding=encoding, errors='replace') as file:
        lines = file.readlines()

    seen = set()
    unique_lines = []
    duplicate_count = 0

    for line in lines:
        if line in seen:
            duplicate_count += 1
        else:
            seen.add(line)
            unique_lines.append(line)

    if sort_lines:
        unique_lines.sort()

    with open(output_file, 'w', encoding=encoding) as file:
        file.writelines(unique_lines)

    return duplicate_count, len(unique_lines)

def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Remove duplicate lines from a text file and sort unique lines."
    )
    parser.add_argument(
        "-i", "--input",
        dest="input_file",
        default="input.txt",
        help="Path to the input text file (default: input.txt)"
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        default="new.txt",
        help="Path to the output cleaned text file (default: new.txt)"
    )
    parser.add_argument(
        "--keep-order",
        dest="sort_lines",
        action="store_false",
        help="Preserve original order instead of sorting lines alphabetically"
    )
    parser.add_argument(
        "--no-clear",
        dest="clear_screen",
        action="store_false",
        help="Do not clear the terminal before printing report"
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="File encoding (default: utf-8)"
    )
    return parser.parse_args(args)

def main():
    args = parse_args()

    if not os.path.exists(args.input_file):
        print(f"\033[31mError: Input file '{args.input_file}' not found.\033[0m", file=sys.stderr)
        print("Please provide a valid input file via -i / --input or ensure 'input.txt' exists.", file=sys.stderr)
        sys.exit(1)

    try:
        duplicate_count, unique_count = remove_duplicates(
            args.input_file,
            args.output_file,
            sort_lines=args.sort_lines,
            encoding=args.encoding
        )
    except Exception as e:
        print(f"\033[31mError processing file: {e}\033[0m", file=sys.stderr)
        sys.exit(1)

    if args.clear_screen:
        clear_terminal()

    # Beautiful output to the terminal
    print("\033[1m" + "Duplication Removal Report" + "\033[0m")  # Bold title
    print("-" * 30)
    print(f"Total Lines Processed: \033[32m{duplicate_count + unique_count}\033[0m")  # Green for total lines
    print(f"Unique Lines: \033[34m{unique_count}\033[0m")  # Blue for unique count
    print(f"Duplicate Lines: \033[31m{duplicate_count}\033[0m")  # Red for duplicate count
    print("-" * 30)
    print(f"Corrected file saved as \033[33m{args.output_file}\033[0m.")  # Yellow for file path

if __name__ == '__main__':
    main()
