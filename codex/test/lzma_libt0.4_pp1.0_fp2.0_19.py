import lzma
lzma.open

import os
import os.path

import re


#
# Constants
#

#
# Global variables
#

#
# Functions for external use
#

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate a list of files in a directory tree.')
    parser.add_argument('-i', '--input', metavar='input_directory', required=True, help='Input directory')
    parser.add_argument('-o', '--output', metavar='output_file', required=True, help='Output file')
    parser.add_argument('-c', '--compression', metavar='compression_level', type=int, default=9, help='Compression level')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.verbose:
        print('Input directory:', args.input)
       
