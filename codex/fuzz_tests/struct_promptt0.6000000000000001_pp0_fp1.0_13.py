import _struct
# Test _struct.Struct

import _struct as struct

def test_struct(fmt, val, bigendian):
    s = struct.Struct(fmt)
    if bigendian:
        s = s.bigendian()
    sval = s.pack(val)
    assert s.size == len(sval)
    uval = s.unpack(sval)
    assert uval == (val,)
    assert s.unpack_from(sval) == uval
    assert s.unpack_from(sval, 0) == uval
    assert s.unpack_from(buffer(sval, 0)) == uval
    assert s.unpack_from(sval, 0, 1) == uval[:1]
    assert s.unpack_from(sval, 1) == uval[1:]
    assert s.unpack_from(sval, 1, 1) == uval[1:2]

def test_struct_endianness(fmt, val, bigendian):
    s = struct.Struct(fmt)
    if bigend
