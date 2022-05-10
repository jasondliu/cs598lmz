from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# bz2
import bz2
compressed = bz2.compress(data)
bz2.decompress(compressed)

# zlib
import zlib
compressed = zlib.compress(data)
zlib.decompress(compressed)

# LZMA
from lzma import compress, decompress
compressed = compress(data)
decompress(compressed)

# bz2
import bz2
compressed = bz2.compress(data)
bz2.decompress(compressed)

# zlib
import zlib
compressed = zlib.compress(data)
decompressed = zlib.decompress(compressed)
original == decompressed

# lzma
from lzma import open

with open('file.xz', 'rb') as input, \
     open('file.txt', 'wb') as output:
    for line in input:
        output.write(line)

# gzip
import gzip

with
