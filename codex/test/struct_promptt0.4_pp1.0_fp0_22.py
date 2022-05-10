import _struct
# Test _struct.Struct

def pack(fmt, *args):
    s = _struct.Struct(fmt)
    return s.pack(*args)

def unpack(fmt, *args):
    s = _struct.Struct(fmt)
    return s.unpack(*args)

def calcsize(fmt):
    s = _struct.Struct(fmt)
    return s.size

def test_struct_unpack():
    assert unpack('i', pack('i', 1)) == (1,)
    assert unpack('hh', pack('hh', 1, 2)) == (1, 2)
    assert unpack('hhh', pack('hhh', 1, 2, 3)) == (1, 2, 3)
    assert unpack('bBhHiIlLqQfd', pack('bBhHiIlLqQfd', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.0, 12.0)) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.0, 12.0)
