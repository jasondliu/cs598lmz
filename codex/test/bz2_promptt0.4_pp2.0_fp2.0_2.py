import bz2
# Test BZ2Decompressor
#
# This example shows how to use the BZ2Decompressor class to decompress a
# stream of data.

# Open the compressed file
filename = "test.bz2"
f = bz2.BZ2File(filename, 'r')

# Create a decompressing object
decompressor = bz2.BZ2Decompressor()

# Read one compressed block at a time
