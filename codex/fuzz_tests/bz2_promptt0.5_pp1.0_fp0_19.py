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
assert c.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'
                    b'\x2d\x52\x4d\x4c\x4a\x4e\x2d\x52\x4d\x4c\x4a\x4e') == b''
assert c.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'
                    b'\x2d\x52\x4
