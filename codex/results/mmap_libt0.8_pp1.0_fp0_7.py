import mmap
import sys
import argparse

def parse_args():
	parser = argparse.ArgumentParser(description='Generate QR Codes from a list of URLs')
	parser.add_argument('--url-file', required=True, help='Path to URL file (one URL per line)')
	parser.add_argument('--header', action='store_true', help='Skip first line (assume it is a header)')
	parser.add_argument('--limit', type=int, help='Limit to a certain number of URLs')
	parser.add_argument('--out-dir', required=True, help='Path to output directory')
	return parser.parse_args()

args = parse_args()

# Check that URL file exists
if not os.path.isfile(args.url_file):
	print("Invalid input file: {}".format(args.url_file))
	sys.exit(1)

# Check that output directory exists
if not os.path.isdir(args.out_dir):
	print("Invalid output directory: {}".format(args.out_dir
