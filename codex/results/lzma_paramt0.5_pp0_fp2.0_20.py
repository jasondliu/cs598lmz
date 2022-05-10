from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

import bz2
bz2.decompress(compressed_data)

import zlib
zlib.decompress(compressed_data)

import gzip
with gzip.open('compressed_data.gz', 'rb') as f:
    f.read()
