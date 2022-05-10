from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# The bz2 module includes a utility function to decompress a file
import bz2
uncompressed_data = bz2.decompress(bz2_data)

# The bz2 module also includes a one-shot class that can be used to decompress data without creating a decompressor object
uncompressed_data = bz2.decompress(bz2_data)

# The bz2 module provides a BZ2File class that represents a file compressed using BZIP2
# BZ2File implements the same interface as the built-in open function
with bz2.open('file.bz2', 'rt') as input:
    print(input.read())

# BZ2File can also be used to write compressed data
with bz2.open('file.bz2', 'wt') as output:
    output.write(text)

# BZ2File can also be used as a context manager for compressing and decompressing data in memory
with bz2.open('file.bz2', '
