from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# compress
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(data)
compressor.flush()

# -*- coding: utf-8 -*-
from bz2 import BZ2File
with BZ2File('example.bz2', 'wb') as output:
    output.write(b'Contents of the example file go here.\n')

with BZ2File('example.bz2', 'rb') as input:
    print(input.read())

# lzma
import lzma
with lzma.open('example.xz', 'wt') as output:
    output.write('Contents of the example file go here.\n')

with lzma.open('example.xz', 'rt') as input:
    print(input.read())

# zlib
import zlib
compressed_data = zlib.compress(data)
original_data = zlib.decompress(compressed_data)
