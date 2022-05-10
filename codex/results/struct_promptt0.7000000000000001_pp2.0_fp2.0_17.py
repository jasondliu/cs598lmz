import _struct
# Test _struct.Struct separately from the rest of the _struct module,
# to avoid confusion about what gets tested where.
import test.support

# Test _struct.Struct

# example usage for calcsize and pack
with test.support.check_py3k_warnings():
    import struct, array

def test_struct():
    fmt = 'hhl'
    s = _struct.Struct(fmt)
    got = s.size
    expected = struct.calcsize(fmt)
    assert got == expected

    args = (1, 2, 3)
    got = s.pack(*args)
    expected = struct.pack(fmt, *args)
    assert got == expected

    got = s.pack_into(array.array('b', b'xxxx'), 1, *args)
    expected = struct.pack_into(fmt, array.array('b', b'xxxx'), 1, *args)
    assert got == expected

    got = s.unpack(got)
    expected = struct.unpack(fmt, expected)
    assert got == expected

    got = s.
