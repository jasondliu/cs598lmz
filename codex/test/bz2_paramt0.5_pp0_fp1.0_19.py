from bz2 import BZ2Decompressor
BZ2Decompressor()

from lzma import LZMADecompressor
LZMADecompressor()

# Test that the zlib module is functional
import zlib
assert zlib.decompress(zlib.compress(b"test")) == b"test"

# Test that the gzip module is functional
import gzip
assert gzip.decompress(gzip.compress(b"test")) == b"test"

# Test that the bz2 module is functional
import bz2
assert bz2.decompress(bz2.compress(b"test")) == b"test"

# Test that the lzma module is functional
import lzma
assert lzma.decompress(lzma.compress(b"test")) == b"test"

# Test that the bz2 module is functional
import bz2
assert bz2.decompress(bz2.compress(b"test")) == b"test"

# Test that the lzma module is functional
import lzma
