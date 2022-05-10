import _struct
# Test _struct.Struct.

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == len(expected)
    assert s.pack(*range(len(expected))) == expected
    assert s.unpack(expected) == tuple(range(len(expected)))
    assert s.unpack_from(expected) == tuple(range(len(expected)))
    assert s.unpack_from(expected, 1) == tuple(range(1, len(expected)))
    assert s.unpack_from(expected, len(expected)) == ()
    assert s.unpack_from(expected, len(expected)+1) == ()
    assert s.unpack_from(expected, -1) == ()
    assert s.unpack_from(expected, -2) == (len(expected)-1,)
    assert s.unpack_from(expected, -len(expected)) == tuple(range(len(expected)))

test_struct('b', b'\x00\x01\x02')
test_struct('B', b'\x00\x01\
