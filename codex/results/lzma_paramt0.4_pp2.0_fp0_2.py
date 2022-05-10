from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# bz2
import bz2
bz2.decompress(compressed)

# zlib
import zlib
zlib.decompress(compressed)

# gzip
import gzip
gzip.decompress(compressed)
