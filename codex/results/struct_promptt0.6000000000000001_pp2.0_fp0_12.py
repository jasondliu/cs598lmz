import _struct
# Test _struct.Struct.pack_into().
def test_pack_into():
    s = _struct.Struct('i')
    buf = bytearray(20)
    s.pack_into(buf, 0, 1)
    s.pack_into(buf, 4, 2)
    s.pack_into(buf, 8, 3)
    assert buf == b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
