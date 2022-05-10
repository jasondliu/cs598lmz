import _struct
# Test _struct.Struct.
def test_struct():
    # Test big-endian formats.
    s = _struct.Struct('>i')
    assert s.size == 4
    assert s.pack(10) == b'\x00\x00\x00\n'
    assert s.pack(-1) == b'\xff\xff\xff\xff'
    assert s.unpack(b'\x00\x00\x00\n') == (10,)
    assert s.unpack(b'\xff\xff\xff\xff') == (-1,)
    assert s.unpack(b'\x00\x00\x00\n\xff\xff\xff\xff') == (10, -1)
    # Test little-endian formats.
    s = _struct.Struct('<i')
    assert s.size == 4
    assert s.pack(10) == b'\n\x00\x00\x00'
    assert s.pack(-1) == b'\xff\xff\xff\xff'
    assert s.unpack(b'\n\
