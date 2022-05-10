import mmap
import os
import re

def usage():
    print("Usage: python3 {} [infile] [outfile] [min_length] [max_length]".format(
        sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        usage()

    infile = sys.argv[1]
    outfile = sys.argv[2]
    min_length = int(sys.argv[3])
