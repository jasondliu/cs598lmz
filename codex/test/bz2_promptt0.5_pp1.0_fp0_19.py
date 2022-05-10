import bz2
# Test BZ2Decompressor
#
# This program tests the BZ2Decompressor class.

from bz2 import BZ2Decompressor

# Test decompression of multiple streams

c = BZ2Decompressor()

# The empty string is a valid compressed stream.
assert c.decompress(b'') == b''

# Repeated calls to decompress() should return empty bytes.
assert c.decompress(b'') == b''
