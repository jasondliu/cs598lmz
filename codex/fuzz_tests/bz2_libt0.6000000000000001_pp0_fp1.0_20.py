import bz2
bz2.BZ2File.readlines = lambda self: self.read().decode().splitlines(True)

import sys

# get the filename from the command line
if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], "filename")
    exit(1)

filename = sys.argv[1]

print("reading from", filename)

# open the bz2 file and read the lines
with bz2.BZ2File(filename) as infile:
    for line in infile:
        print(line, end = '')
