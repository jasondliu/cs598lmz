import bz2
# Test BZ2Decompressor on data from a file

with bz2.open('sample.bz2', 'rb') as input:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda : input.read(100 * decompressor.decompress(input.read(100))), b''):
        print(block)

# Get the size of the decompressed data

import bz2
import os

original_size = os.path.getsize('sample.bz2')
with bz2.open('sample.bz2', 'rb') as input:
    with open('sample.csv', 'wb') as output:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

uncompressed_size = os.path.getsize('sample.csv')

print('Original is %s, uncompressed to %s' % (original_size, uncompressed_size))


# Compress
