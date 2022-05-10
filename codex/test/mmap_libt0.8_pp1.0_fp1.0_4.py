import mmap
import json
import os

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <mapping_file>")
        exit(1)

    # Get input file
    mapping_file = sys.argv[1]

    # Open file and map to memory
    with open(mapping_file, 'r') as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

        # Read the file line by line
