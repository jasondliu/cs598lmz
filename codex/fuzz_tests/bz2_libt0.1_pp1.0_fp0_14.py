import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# You can also use bz2.BZ2Compressor and bz2.BZ2Decompressor objects for incremental compression and decompression.

# The zlib module provides a lower-level interface to many of the functions in the zlib compression library from GNU.
# The zlib.compress() function returns a bytes object containing compressed data.
# The zlib.decompress() function returns a bytes object containing the uncompressed data.

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# The lzma module contains:
#
# class lzma.LZMAFile(filename=None, mode="r", fileobj=None, format=None, check=-1
