import _struct
# Test _struct.Struct.

def test_struct():
    s = _struct.Struct('l')
    assert s.size == 4
    assert s.pack(37) == b'%c%c%c%c' % (37,0,0,0)
    assert s.unpack(b'%c%c%c%c' % (37,0,0,0)) == (37,)
    raises(_struct.error, s.pack, 37, 38, 39)
    raises(_struct.error, s.unpack, b'x' * 3)
    #
    s = _struct.Struct('llllll')
    assert s.size == 24
    assert s.pack(1, 2, 3, 4, 5, 6) == b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00'
    assert s.unpack(
