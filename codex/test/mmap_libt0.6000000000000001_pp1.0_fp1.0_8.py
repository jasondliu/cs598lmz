import mmap
import sys

def main(argv):
    filename = argv[1]
    with open(filename, "r+b") as f:
        # memory-map the file, size 0 means whole file
        mm = mmap.mmap(f.fileno(), 0)
        # read content via standard file methods
        mm.seek(0)
