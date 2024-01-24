import sys
##python convert.py test.txt gg.txt

def process_file(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Convert to uppercase
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_file}' successfully processed. Result saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    # Check if an input file and output file are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_file(input_file, output_file)
