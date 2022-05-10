import bz2
bz2.decompress(bz2.compress(b'Hello World'))

# bz2.compress() compresses the data and returns a bytes object.
# bz2.decompress() decompresses the data and returns a bytes object.

# Compression with bz2 is generally slower than with gzip, but the compressed
# files are usually smaller.

# The bz2 module also provides an incremental compression and decompression
# interface, in the form of BZ2Compressor and BZ2Decompressor objects.

# In addition to the standard compression and decompression functions, the
# bz2 module defines a class called BZ2File that represents a file that uses
# the bzip2 compression algorithm.

# BZ2File objects have a write() method that can be used to write compressed
# data to a file.

with bz2.BZ2File('compressed.bz2', 'w') as f:
    f.write(b'Hello World')

# The BZ2File class also has a read() method for reading the compressed data.

with b
