from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_bytes)

import bz2
bz2.decompress(bz2_bytes)

import snappy
snappy.uncompress(snappy_bytes)

import zstandard as zstd
decompressor = zstd.ZstdDecompressor()
decompressor.decompress(zstd_bytes)

import zlib
zlib.decompress(zlib_bytes)

# LZMA and BZ2 can also be decompressed with gzip, and
# snappy, zstd and zlib can also be decompressed with deflate
# and vice versa.
