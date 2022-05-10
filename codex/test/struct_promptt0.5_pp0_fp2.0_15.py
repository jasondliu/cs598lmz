import _struct
# Test _struct.Struct
def test_struct():
    s = _struct.Struct('I')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(2) == b'\x02\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x02\x00\x00\x00') == (2,)
    s = _struct.Struct('i')
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(2) == b'\x02\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x02\x00\x00\x00') == (2,)
    s = _struct.Struct('i')

