from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(x)

# Compression using LZMA algorithm
# https://docs.python.org/3/library/lzma.html
import lzma
x = lzma.compress(b"Hello")
lzma.decompress(x)

# Python 3.4+ comes with a simple LZMA file compressor
import shutil
with lzma.open('file.xz', 'wt') as f:
    f.write("Hello")

# Compression using the zlib library
# https://docs.python.org/3/library/zlib.html
import zlib
x = zlib.compress(b"Hello")
zlib.decompress(x)

# Compression using the bzip2 library
# https://docs.python.org/3/library/bz2.html
import bz2
x = bz2.compress(b"Hello")
bz2.decompress(x)

# Python 3.3+ comes with a simple bzip2 file compressor
import shutil
with bz2.
