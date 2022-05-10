import bz2
# Test BZ2Decompressor
#
# This program tests the BZ2Decompressor class.
#

from bz2 import BZ2Decompressor

d = BZ2Decompressor()

# Read in a file containing a few blocks of compressed data.
f = open("testdata.bz2", "rb")

# Decompress each block in turn.
while True:
    block = f.read(1024)
    if not block:
        break
    print(d.decompress(block))

# Decompress any remaining data.
print(d.flush())
