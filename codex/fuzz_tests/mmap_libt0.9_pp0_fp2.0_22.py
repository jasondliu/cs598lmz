import mmap
from collections import defaultdict
from operator import itemgetter
import glob
import os
os.sys.path.append('../out/')
from helpers import *
def FastqIterator(handle):
    "Read fastq entry"
    while handle:
        name = handle.readline()
        if not name:
            break
        name = name[1:].strip()
        seq = handle.readline()
        if not seq:
            break
        seq = seq.strip()
        handle.readline()
        qual = handle.readline()
        if not qual:
            break
        qual = qual.strip()
        yield [name, seq, qual]


if __name__ == "__main__":
    if len(os.sys.argv) < 5:
        print("Given a fastq file and a taxon, compute the read identity to that taxon")
        print("Usage: python ReadIdentity.py output left.fastq right.fastq")
        os.sys.exit()

    output_file = os.sys.argv[1]
    
   
