import _struct
# Test _struct.Struct

# Bug #834455: _struct.Struct was not working properly with the 's' format.

import _struct

class X(object):
    pass

def test_struct(format, expected):
    s = _struct.Struct(format)
    assert s.size == len(expected)
    assert s.pack(*range(len(expected))) == expected

def test_unpack(format, expected, data):
    s = _struct.Struct(format)
    assert s.unpack(data) == expected

def test_unpack_iter(format, expected, data):
    s = _struct.Struct(format)
    assert list(s.iter_unpack(data)) == [expected]

def test_unpack_iter_overflow(format, expected, data):
    s = _struct.Struct(format)
    assert list(s.iter_unpack(data)) == [expected]
    assert list(s.iter_unpack(data)) == [expected]

