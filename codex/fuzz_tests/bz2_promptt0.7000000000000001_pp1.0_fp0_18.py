import bz2
# Test BZ2Decompressor
#
# Create an instance of BZ2Decompressor.
# Read the compressed data from a file and write the uncompressed data to a
# file.

import os
import bz2

with open('example.bz2', 'rb') as infile:
    with open('example.out', 'wb') as outfile:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: infile.read(100 * 1024), b''):
            outfile.write(decompressor.decompress(data))

print('The original file ' + str(os.stat('example.bz2').st_size) +
      ' bytes long')
print('The decompressed file ' + str(os.stat('example.out').st_size) +
      ' bytes long')
# Example: Compress data
#
# Create an instance of BZ2Compressor.
# Read the uncompressed data from a file and write the compressed data to
# another file.

import os
import bz2

with open('example.txt', '
