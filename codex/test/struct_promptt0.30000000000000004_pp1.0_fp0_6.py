import _struct
# Test _struct.Struct()

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == struct.calcsize(fmt)
    assert s.format == fmt
    assert s.unpack(expected) == (1, 2, 3)
    assert s.pack(1, 2, 3) == expected

test_struct('hhl', b'\x01\x00\x02\x00\x00\x00\x03\x00')
test_struct('hhl', b'\x01\x00\x02\x00\x00\x00\x03\x00')
test_struct('hhh', b'\x01\x00\x02\x00\x03\x00')
test_struct('hhh', b'\x01\x00\x02\x00\x03\x00')
test_struct('bbb', b'\x01\x02\x03')
test_struct('bbb', b'\x01\x02\x03')
