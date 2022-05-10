import _struct
# Test _struct.Struct

# Test the basic methods

def test_basic():
    s = _struct.Struct('i')
    assert s.size == _struct.calcsize('i')
    assert s.format == 'i'
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0, 1) == (1,)
    assert s.pack_into(b'\x00'*4, 0, 1) == None
    assert b'\x01\x00\x00\x00' == b'\x00'*4
