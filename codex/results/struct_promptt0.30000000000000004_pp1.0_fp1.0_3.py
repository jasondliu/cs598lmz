import _struct
# Test _struct.Struct.pack_into()

def test_pack_into():
    s = _struct.Struct('hhl')
    b = bytearray(s.size)
    s.pack_into(b, 0, 1, 2, 3)
    assert b == b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00'
    s.pack_into(b, 0, 1, 2, 3)
    assert b == b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00'
    s.pack_into(b, 1, 1, 2, 3)
    assert b == b'\x01\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00'
    s.pack_into(b, 2, 1, 2, 3)
    assert b == b'\x01
