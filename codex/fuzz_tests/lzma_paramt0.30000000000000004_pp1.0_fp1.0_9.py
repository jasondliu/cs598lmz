from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bz2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# zlib
import zlib
zlib.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# snappy
import snappy
snappy.decompress(data)

# lz4
import lz4
lz4.decompress(data)

# lz4framed
import lz4framed
lz4framed.decompress(data)

# lz4.block
import lz4.block
lz4.block.decompress(data)

# lz4.frame
import lz4.frame
lz4.frame.decompress(data)

# lz4.block
import lz4.block
lz4.block.decompress(data)

# l
