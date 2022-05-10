import mmap
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <file>" % sys.argv[0])
        sys.exit(1)

    fname = sys.argv[1]
    fsize = os.stat(fname).st_size

    with open(fname, 'r+b') as f:
        mm = mmap.mmap(f.fileno(), fsize)

        # Replace the first character of the file with 'X'
        mm[0] = 'X'

        # Close the mmap instance
        mm.close()

