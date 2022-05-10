import mmap
import heapq
import logging
import argparse
import os
import sys
import time

from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description="Sorting large file")
    parser.add_argument("-i", "--infile", help="Input file", required=True)
    parser.add_argument("-c", "--chunks", help="Input file", required=True)
    parser.add_argument("-o", "--outfile", help="Output file", required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)s: %(message)s')

    sort_large(args.infile, args.outfile, int(args.chunks))


