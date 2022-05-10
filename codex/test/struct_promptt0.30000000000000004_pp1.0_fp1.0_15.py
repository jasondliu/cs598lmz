import _struct
# Test _struct.Struct

# Test the basic methods

def test_basic():
    s = _struct.Struct('i')
    eq(s.size, 4)
    eq(s.pack(1), b'\x01\x00\x00\x00')
    eq(s.unpack(b'\x01\x00\x00\x00'), (1,))
    eq(s.unpack_from(b'\x01\x00\x00\x00', 0), (1,))
    eq(s.unpack_from(b'\x01\x00\x00\x00', 1), (16777216,))
    eq(s.unpack_from(b'\x01\x00\x00\x00', 2), (4278190080,))
    eq(s.unpack_from(b'\x01\x00\x00\x00', 3), (4294967295,))
