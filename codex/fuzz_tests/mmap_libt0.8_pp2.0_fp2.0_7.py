import mmap
from collections import Counter
import scipy.io
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-k', help = "length of k-mer", required = True, type = int)
parser.add_argument('-i', help = "Input File", required = True, type = str)
parser.add_argument('-o', help = "Output File", required = True, type = str)

args = parser.parse_args()
kmer_counts = Counter()

with open(args.i, 'r') as f:
    for line in f:
        for i in range(len(line[0:-1]) - args.k + 1):
            kmer_counts[line[i:i + args.k]] += 1

scipy.io.mmwrite(args.o, kmer_counts)
