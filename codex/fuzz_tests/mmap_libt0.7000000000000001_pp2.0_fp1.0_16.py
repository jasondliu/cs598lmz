import mmap
import argparse
import sys
import random
import heapq
import math

parser = argparse.ArgumentParser(description='Get kmer count distribution of the input sequence file.')
parser.add_argument('-i', metavar='input', type=str, nargs=1, help='input sequence file')
parser.add_argument('-k', metavar='kmer', type=int, nargs=1, help='kmer length')
parser.add_argument('-o', metavar='output', type=str, nargs=1, help='output file')
args = parser.parse_args()

def parse_seq_file(file_name):
    with open(file_name, "r+b") as f:
        # memory-map the file, size 0 means whole file
        mm = mmap.mmap(f.fileno(), 0)
        line = mm.readline()
        cnt = 0
        while line:
            yield line.rstrip()
            line = mm.readline()
            cnt += 1
        mm.close()

