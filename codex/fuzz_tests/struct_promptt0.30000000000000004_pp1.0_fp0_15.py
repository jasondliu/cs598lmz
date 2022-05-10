import _struct
# Test _struct.Struct.

# Test the basic methods of _struct.Struct.

import _struct
import sys

def test_basic():
    # Test the basic methods of _struct.Struct.
    s = _struct.Struct('hhl')
    eq(s.size, 8)
    eq(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')
    eq(s.pack_into(bytearray(12), 4, 1, 2, 3), None)
    eq(bytes(bytearray(12)), b'\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x03')
    eq(s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
    eq(s.unpack_from(b'\x00\x00\x00\x00\x01\
