from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.open()
# bz2.compress()
# bz2.decompress()

# The bz2.open() function works like open() but returns a BZ2File object
# that can be used for reading or writing compressed data.

# The compress() function takes a byte string as input and returns a byte string
# containing the compressed data.

# The decompress() function takes a byte string containing compressed data as input
# and returns a byte string containing the uncompressed data.

# The compress() and decompress() functions only work with byte strings.
# For Unicode text, use the compress() and decompress() methods of BZ2Compressor
# and BZ2Decompressor objects.

# For example, here is how to compress a sequence of Unicode strings:

import bz2
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\
