from lzma import LZMADecompressor
LZMADecompressor().decompress(b)

# xz

from lzma import LZMADecompressor
LZMADecompressor().decompress(b)

# gzip

from gzip import decompress
decompress(b)

# bzip2

from bz2 import decompress
decompress(b)

# snappy

from snappy import decompress
decompress(b)

# zstandard

from zstandard import decompress
decompress(b)

# brotli

from brotli import decompress
decompress(b)
