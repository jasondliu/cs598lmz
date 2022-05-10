import mmap
import shutil
import time
import hashlib
import os
import sys

#import pysam

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Construct a blast database from a fasta file')
    parser.add_argument('-i', '--input', dest='input', help='input fasta file', required=True)
    parser.add_argument('-o', '--output', dest='output', help='output directory', required=True)
    parser.add_argument('-t', '--taxonomy', dest='taxonomy', help='taxonomy file', required=False)
    parser.add_argument('-f', '--format', dest='format', help='db format', required=True)

    args = parser.parse_args()

    input = args.input
    output = args.output
    taxonomy = args.taxonomy
    format = args.format

    if not os.path.isfile(input):
        print "Input file does not exist"
        sys.exit(1)

    if not os.path.
