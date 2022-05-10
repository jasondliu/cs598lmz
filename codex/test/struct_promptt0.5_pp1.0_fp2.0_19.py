import _struct
# Test _struct.Struct.

def test_pack():
    s = _struct.Struct('i')
    assert s.pack(12345) == b'\x39\x30\x00\x00'
    assert s.pack(-12345) == b'\xc7\xcf\xff\xff'
    assert s.pack(0) == b'\x00\x00\x00\x00'
    assert s.pack(2147483647) == b'\xff\xff\xff\x7f'
    assert s.pack(-2147483648) == b'\x00\x00\x00\x80'

    raises(struct.error, s.pack, 1.0)
    raises(struct.error, s.pack, 'abc')
    raises(struct.error, s.pack, '\x00\x00\x00\x00\x00')
    raises(struct.error, s.pack, '\x00\x00\x00')
