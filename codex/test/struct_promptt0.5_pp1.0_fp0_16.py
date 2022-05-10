import _struct
# Test _struct.Struct()

def test_struct():
    # Test _struct.Struct()
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x00', 4) == (1,)
    assert s.pack_into(b'\x00'*4, 0, 1) == None
    assert s.pack_into(b'\x00'*8, 4, 1) == None
