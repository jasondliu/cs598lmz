import _struct
# Test _struct.Struct

import struct

def test(format, expected, *args):
    s = _struct.Struct(format)
    assert s.size == struct.calcsize(format)
    s = _struct.Struct(format + ' ')
    assert s.size == struct.calcsize(format)
    s = _struct.Struct(' ' + format)
    assert s.size == struct.calcsize(format)
    s = _struct.Struct(' ' + format + ' ')
    assert s.size == struct.calcsize(format)

    s = _struct.Struct(format)
    assert s.pack(*args) == struct.pack(format, *args)
    assert s.unpack(s.pack(*args)) == struct.unpack(format, s.pack(*args))
    assert s.unpack_from(s.pack(*args)) == struct.unpack_from(format, s.pack(*args))
    assert s.unpack_from(s.pack(*args), 0) == struct.unpack_from(format, s.pack(*args), 0)
