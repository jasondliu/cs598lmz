import _struct
# Test _struct.Struct.

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == len(expected)
    assert s.pack(1) == expected
    assert s.unpack(expected) == (1,)
    assert s.unpack_from(expected + expected, 0) == (1,)
    assert s.unpack_from(expected + expected, len(expected)) == (1,)
    assert s.iter_unpack(expected) == [(1,)]
    assert s.iter_unpack(expected + expected) == [(1,), (1,)]
    assert s.iter_unpack(expected + expected, len(expected)) == [(1,)]
    assert s.iter_unpack(expected + expected, len(expected) * 2) == []
    assert s.iter_unpack(expected + expected, len(expected),
                         len(expected)) == [(1,)]

test_struct('x', b'\x00')
test_struct('c', b'\x01')
test_struct('b', b'\x
