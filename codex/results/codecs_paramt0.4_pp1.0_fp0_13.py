import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate a list of all the files in the given directory and all its subdirectories.')
parser.add_argument('directory', metavar='directory', type=str, help='the directory to scan')
parser.add_argument('-o', '--output', metavar='output', type=str, help='the file to output')
args = parser.parse_args()

# Get the directory to scan
directory = args.directory

# Get the output file
output = args.output

# Get a list of all the files in the directory and its subdirectories
files = []
for root, dirs, dir_files in os.walk(directory):
    for file in dir_files:
        files.append(os.path.join(root, file))

# Write the list of files to the output file
if output is not None:
    with open(output, 'w') as f:
        for file in files:
            f.write(file + '
