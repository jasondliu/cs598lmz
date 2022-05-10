import lzma
lzma.LZMA_VERSION

from lzma import *

compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()

decompressor = LZMADecompressor()
data = decompressor.decompress(compressed_data)
data += decompressor.unconsumed_tail

import zlib
zlib.ZLIB_VERSION

from zlib import *

compressor = zlib.compressobj()
compressed_data = compressor.compress(b"some data")
compressed_data += compressor.flush()

decompressor = zlib.decompressobj()
decompressed_data = decompressor.decompress(compressed_data)

import bz2
bz2.BZ2_VERSION

from bz2 import *

compressor = bz2.BZ2Compressor()
compressor.compress(b"some data")
compressor.flush()

decompressor = BZ2Decompressor()
data = decompressor.decompress(
