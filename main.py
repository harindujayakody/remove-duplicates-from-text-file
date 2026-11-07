import argparse
import os
import sys

def clear_terminal():
    # Clear the terminal screen
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

def remove_duplicates(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Track the count of duplicate lines
    seen = set()
    unique_lines = []
    duplicate_count = 0

    for line in lines:
        if line in seen:
            duplicate_count += 1
        else:
            seen.add(line)
            unique_lines.append(line)

    # Sort the unique lines in ascending order
    unique_lines.sort()

    # Write the sorted unique lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

    # Return the count of duplicates and the count of unique lines
    return duplicate_count, len(unique_lines)

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Remove duplicate lines from a text file."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="input.txt",
        help="Text file to read (default: input.txt)",
    )
    parser.add_argument(
        "-o", "--output",
        default="new.txt",
        help="File to write the unique lines to (default: new.txt)",
    )
    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    if not os.path.exists(args.input_file):
        print(f"Error: input file '{args.input_file}' does not exist.", file=sys.stderr)
        return 2

    # Clear the terminal screen
    clear_terminal()

    try:
        duplicate_count, unique_count = remove_duplicates(args.input_file, args.output)
    except OSError as error:
        print(f"Error: could not process files: {error}", file=sys.stderr)
        return 1

    # Beautiful output to the terminal
    print("\033[1m" + "Duplication Removal Report" + "\033[0m")  # Bold title
    print("-" * 30)
    print(f"Total Lines Processed: \033[32m{duplicate_count + unique_count}\033[0m")  # Green for total lines
    print(f"Unique Lines: \033[34m{unique_count}\033[0m")  # Blue for unique count
    print(f"Duplicate Lines: \033[31m{duplicate_count}\033[0m")  # Red for duplicate count
    print("-" * 30)
    print(f"Corrected file saved as \033[33m{args.output}\033[0m.")  # Yellow for file path
    return 0

if __name__ == "__main__":
    sys.exit(main())
