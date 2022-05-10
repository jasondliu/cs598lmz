from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# The bz2 module includes a function for decompressing a whole file.
with open('example.bz2', 'rb') as input:
    with bz2.open(input, 'rt') as decompressor:
        for line in decompressor:
            print(line)


# The zlib module provides a lower-level interface based on the inflate algorithm.

import zlib

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)


# -----------------------------------------------------------------------------
# 7.6. Using LZMA for Compression
# -----------------------------------------------------------------------------

import lzma

data = b'witch which has which witches wrist watch'

with lzma.open('compress.xz', 'w') as f:
    f.write(data)

with lzma.open('compress.xz') as f:
    file_content = f
