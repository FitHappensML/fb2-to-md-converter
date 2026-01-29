# cli.py (Updated)

# Import necessary libraries
import argparse # For parsing command-line arguments
import os       # For working with file paths

# Import our core conversion function from converter.py
from converter import convert_fb2_to_txt

def main():
    """
    Main function to run the command-line interface.
    """
    # --- 1. Set up the Argument Parser ---
    parser = argparse.ArgumentParser(
        description="A simple tool to convert FB2 files to TXT or MD format."
    )

    # Argument 1: input_file (positional, required)
    parser.add_argument(
        "input_file",
        help="Path to the input FB2 file."
    )

    # Argument 2: output_file (positional, optional)
    parser.add_argument(
        "output_file",
        nargs="?",
        # UPDATED: Help text now mentions the appropriate extension.
        help="Path to the output file (optional). "
             "If not specified, it will be saved next to the input file with the chosen format's extension."
    )

    # --- NEW: Argument for format selection ---
    # REPLACED the old '--smart-formatting' flag with a more versatile '--format' option.
    parser.add_argument(
        "-f", "--format",
        choices=['txt', 'md'],
        default='txt',
        help="The output format ('txt' for plain text, 'md' for Markdown). Default is 'txt'."
    )

    # Parse the arguments provided by the user in the command line
    args = parser.parse_args()

    # --- 2. Process the Arguments ---
    input_path = args.input_file
    output_path = args.output_file

    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at '{input_path}'")
        return

    # --- UPDATED: Dynamic output path based on format ---
    # If the output file path was not provided, create a default one.
    # e.g., 'my_book.fb2' with format 'md' becomes 'my_book.md'.
    if not output_path:
        base_name = os.path.splitext(input_path)[0]
        # Use the format specified by the user for the file extension
        output_path = f"{base_name}.{args.format}"

    # --- 3. Read, Convert, and Save ---
    print(f"Reading from: {input_path}")
    
    try:
        # Open and read the input file's content
        with open(input_path, 'r', encoding='utf-8') as f:
            fb2_content = f.read()

        # --- UPDATED: Logic to set smart_formatting based on format ---
        # Determine if smart formatting should be used.
        # It's 'On' if the user chose 'md', otherwise 'Off'.
        use_smart_formatting = (args.format == 'md')

        print(f"Converting to format: {args.format.upper()}")
        
        # Call our core function with the determined setting
        converted_content = convert_fb2_to_txt(
            fb2_content, 
            smart_formatting=use_smart_formatting
        )

        # Write the resulting text to the output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted_content)

        print(f"Successfully converted and saved to: {output_path}")

    except Exception as e:
        # Catch any potential errors during the process
        print(f"An error occurred: {e}")

# This makes the script executable
if __name__ == "__main__":
    main()