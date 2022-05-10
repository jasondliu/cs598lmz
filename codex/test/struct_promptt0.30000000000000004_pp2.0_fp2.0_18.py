import _struct
# Test _struct.Struct.unpack_from

import array

def test(fmt, data, expected):
    s = _struct.Struct(fmt)
    a = array.array('b', data)
    res = s.unpack_from(a, 0)
