from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bz2
from bz2 import decompress
decompress(data)

# zlib
from zlib import decompress
decompress(data)

# brotli
from brotli import decompress
decompress(data)

# gzip
from gzip import decompress
decompress(data)

# deflate
from zlib import decompress
decompress(data)

# identity
data
