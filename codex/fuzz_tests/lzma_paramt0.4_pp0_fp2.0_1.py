from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# gzip
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'wb') as f:
    f.write(b'Hello World')

import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'wb') as f:
    f.write(b'Hello World')

# Reading and Writing Binary Arrays of Structures
import struct

# Writing binary data
with open('somefile.bin', 'wb') as f:
    data = struct.pack('>i4sh', 7, b'spam', 8)

