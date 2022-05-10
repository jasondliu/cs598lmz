import lzma
lzma.LZMADecompressor().decompress(lzma.LZMACompressor().compress(b'a' * 1000))

import bz2
bz2.BZ2Decompressor().decompress(bz2.BZ2Compressor().compress(b'a' * 1000))

import zlib
zlib.decompress(zlib.compress(b'a' * 1000))

import gzip
