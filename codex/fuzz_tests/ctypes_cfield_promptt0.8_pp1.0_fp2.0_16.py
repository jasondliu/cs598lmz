import ctypes
# Test ctypes.CField

from ctypes import *
import _ctypes_test

from _ctypes_test import get_types
c_intf = c_int.from_param

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_double)]

def test_fields():
    for typ, result in (
        # basic integer types
        (c_byte, 1),
        (c_short, 2),
        (c_int, 4),
        (c_long, 4),
        (c_longlong, 8),
        (c_ubyte, 1),
        (c_ushort, 2),
        (c_uint, 4),
        (c_ulong, 4),
        (c_ulonglong, 8),
        (c_char, 1),
        (c_char_p, 4),
        (c_wchar, 2),
        (c_wchar_p, 4),
        (c_float, 4),
        (c_double, 8),
        (c_longdouble, 8),
