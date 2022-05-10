from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bzip2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# zlib
import zlib
zlib.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# bz2
import bz2
bz2.decompress(data)

# zstandard
import zstandard as zstd
zstd.ZstdDecompressor().decompress(data)

# brotli
import brotli
brotli.decompress(data)

# blosc
import blosc
blosc.decompress(data)

# lz4
import lz4
lz4.decompress(data)

# snappy
import snappy
snappy.decompress(data)

# zopfli
import zopfli
zopfli.decompress(data)
