import _struct
# Test _struct.Struct.

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == len(expected)
    assert s.pack(*range(len(expected))) == expected
    assert s.unpack(expected) == tuple(range(len(expected)))

test_struct('c', b'\x00')
test_struct('b', b'\x00')
test_struct('B', b'\x00')
test_struct('h', b'\x00\x00')
test_struct('H', b'\x00\x00')
test_struct('i', b'\x00\x00\x00\x00')
test_struct('I', b'\x00\x00\x00\x00')
test_struct('l', b'\x00\x00\x00\x00')
test_struct('L', b'\x00\x00\x00\x00')
test_struct('q', b'\x00\x00\x00\x00\x00\x
