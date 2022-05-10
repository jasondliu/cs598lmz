import _struct
# Test _struct.Struct

def test_Struct():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.format == 'i'
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 3) == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 4) == ()
    assert s.unpack_from(b'\x00\x00\x00*', 5) == ()
    assert s.pack_into(b'\x00\x00\x00\x00\x00\x00\x00\x00', 3, 42) == None
    assert b'\x00\x00\x00*\x00\x
