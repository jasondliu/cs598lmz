import lzma
lzma.decompress(lzma.compress(b'Hello World'))

# lzma.LZMACompressor
# lzma.LZMADecompressor

import bz2
bz2.compress(b'Hello World')
bz2.decompress(bz2.compress(b'Hello World'))

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

import zlib
zlib.compress(b'Hello World')
zlib.decompress(zlib.compress(b'Hello World'))

# zlib.compressobj
# zlib.decompressobj
