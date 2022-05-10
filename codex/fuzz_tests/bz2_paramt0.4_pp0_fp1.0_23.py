from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# The bz2 module includes a BZ2Compressor and BZ2Decompressor class
# that can be used to incrementally compress and decompress data
# using the bzip2 algorithm.

# For example, the following code reads a file and writes it
# back out as a compressed file:

import bz2

uncompressed_data = open('lorem.txt', 'rt').read()
compressed_data = bz2.compress(uncompressed_data.encode('utf-8'))

with open('lorem.bz2', 'wb') as f:
    f.write(compressed_data)

# The compressed file can then be read back in and decompressed like this:

with open('lorem.bz2', 'rb') as f:
    compressed_data = f.read()

uncompressed_data = bz2.decompress(
