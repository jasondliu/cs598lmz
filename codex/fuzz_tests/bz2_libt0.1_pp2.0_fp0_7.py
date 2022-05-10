import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# You can also use bz2.BZ2Compressor and bz2.BZ2Decompressor objects to compress and decompress data streams.

# The zlib module provides a lower-level interface, based on the deflate algorithm.
# It is a bit more complicated to use than bz2 but often a bit faster.

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# The lzma module provides support for the LZMA compression algorithm, which has a high compression ratio and can produce
# compressed files that are typically smaller than bz2 files.

import lzma
s = b'witch which has which witches wrist watch'
len(s)

t
