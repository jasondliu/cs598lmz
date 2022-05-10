import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# You can also use bz2.BZ2Compressor and bz2.BZ2Decompressor objects for incremental compression and decompression.

# The zlib module provides a lower-level interface, compatible with gzip and zlib.
# The zlib.compress() and zlib.decompress() functions provide a simpler interface to compress and decompress data.

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# The binascii module contains a number of methods to convert between binary and various ASCII-encoded binary representations.
# The binascii.hexlify() function is particularly useful for converting binary data into a printable representation.

import binasci
