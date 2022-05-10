import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Convert a .dat file to .csv.')
parser.add_argument('input_file', help='The .dat file to convert.')
parser.add_argument('output_file', help='The .csv file to write.')
parser.add_argument('-f', '--force', action='store_true', help='Overwrite existing file.')
args = parser.parse_args()

# Check if output file already exists
if os.path.isfile(args.output_file):
    if args.force:
        print("Overwriting existing file.")
    else:
        print("Output file already exists. Use -f to overwrite.")
        exit()

# Open input file
with open(args.input_file, 'r', errors="strict") as input_file:
    # Open output file
    with open(args.output_file, 'w') as output_file:
        # Read header
        header = input_file.readline().split()
