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

