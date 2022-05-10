import _struct
# Test _struct.Struct()
import struct

def test_struct(typecode, values, bigendian=False):
    if bigendian:
        prefix = '>'
    else:
        prefix = '<'

    fmt = prefix + typecode
    s = _struct.Struct(fmt)
    got = s.pack(*values)
    expected = struct.pack(fmt, *values)
    assert got == expected

    unpacked = s.unpack(got)
    assert unpacked == values

def test_struct_unpack_from():
    # Test _struct.Struct.unpack_from()
    s = _struct.Struct('<i')
    buf = s.pack(42) + b'after'
    assert s.unpack_from(buf) == (42,)
    assert s.unpack_from(buf, 1) == (0x34333231,)

def test_struct_unpack_from_buffer():
    # Test _struct.Struct.unpack_from() with a buffer
    s = _struct.Struct('<i')
