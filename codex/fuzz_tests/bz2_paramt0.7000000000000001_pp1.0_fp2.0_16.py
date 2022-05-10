from bz2 import BZ2Decompressor
BZ2Decompressor

import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Command line function to extract files from a tar.bz2 file')
parser.add_argument('-x', '--extract', action='store_true',
                    help='Extract all files from the archive. If this option is not given, only the list of files is shown.')
parser.add_argument('-s', '--samples', type=str, default='',
                    help='If you want to extract only a subset of the samples, provide a file with a list of sample identifiers.')
parser.add_argument('-f', '--files', type=str, default='',
                    help='If you want to extract only a subset of the files, provide a file with a list of file names.')
parser.add_argument('-p', '--path', type=str, default='./',
                    help='Optionally, you can provide a path where the files should be extracted. Default: current directory')
parser.add_argument('tbz2', type=str,
                    help='Name of the .
