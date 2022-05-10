from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#
#  lz4
#

from lz4 import LZ4Decompressor
LZ4Decompressor().decompress(data)

#
#  bz2
#

import bz2
bz2.decompress(data)

#
#  zlib
#

import zlib
zlib.decompress(data)

#
#  blosc
#

import blosc
blosc.decompress(data)

#
#  brotli
#

import brotli
brotli.decompress(data)

#
#  zstandard
#

import zstandard
ctx = zstandard.ZstdDecompressor()
ctx.decompress(data)

#
#  zopfli
#

from zopfli import zlib
zlib.decompress(data)
from zopfli import gzip
gzip.decompress(data)
from zopfli import deflate
deflate.decompress(data
