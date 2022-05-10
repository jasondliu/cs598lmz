import _struct
# Test _struct.Struct with the C reached
# through ctypes
import ctypes
import sys

# XXX: This is not a good test, it only tests the
# alignment, but not the size.

align = ctypes.sizeof(ctypes.c_longdouble)

def check_size(fmt, expected):
    s = _struct.Struct(fmt)
    size = s.size
    alignment = s.alignment
    print(size, alignment)
    assert alignment == align
    assert size == expected

def test():
    check_size('P', align)
    check_size('d', align)
    check_size('f', align)
    check_size('i', align)
    check_size('l', align)
    check_size('L', align)
    check_size('Q', align)
    check_size('x', align)
    check_size('h', align)
    check_size('H', align)
    check_size('b', align)
    check_size('B', align)
    check_size('c', align)
    check
