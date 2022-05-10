import _struct
# Test _struct.Struct

def test_struct():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 3) == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 4) == ()
    assert s.unpack_from(b'\x00\x00\x00*', 5) == ()
    assert s.pack_into(b'12345678', 0, 42) == None
    assert b'12345678' == b'*345678'
    assert s.pack_into(bytearray(b'12345678'), 0, 42) == None
    assert bytearray(b
