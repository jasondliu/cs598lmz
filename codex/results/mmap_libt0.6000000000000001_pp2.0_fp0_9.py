import mmap
import sys
from itertools import izip
from itertools import islice
import os
import bz2
from Bio import SeqIO
import gzip

def main():
   parser = argparse.ArgumentParser(description='Remove reads from the fastq file that have a low quality base at the 3\' end')
   parser.add_argument('fastq', help='fastq file')
   parser.add_argument('-q', '--min_quality', type=int, default=20, help='minimum quality')
   parser.add_argument('-l', '--min_length', type=int, default=50, help='minimum length')
   parser.add_argument('-o', '--outfile', help='outfile prefix')
   parser.add_argument('--gzip', action='store_true', help='gzip output')
   parser.add_argument('--bzip2', action='store_true', help='bzip2 output')
   args = parser.parse_args()

   if args.bzip2 and args.gzip:
      sys.st
