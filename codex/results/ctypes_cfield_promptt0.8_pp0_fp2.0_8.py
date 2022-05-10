import ctypes
# Test ctypes.CField methods
from ctypes import (c_short, c_int, c_long, c_longlong,
                    c_ushort, c_uint, c_ulong, c_ulonglong,
                    c_float, c_double, c_char, c_byte,
                    c_char_p, c_void_p, c_wchar, c_wchar_p)

from ctypes import _Pointer

class X(ctypes._Structure):
    _fields_ = [
        ('a', c_short),
        ('b', c_int),
        ('c', c_long),
        ('d', c_longlong),
        ('e', c_ushort),
        ('f', c_uint),
        ('g', c_ulong),
        ('h', c_ulonglong),
        ('i', c_float),
        ('j', c_double),
        ('k', c_char),
        ('l', c_byte),
        ('m', c_char_p),
        ('n', c_void_p),
        ('o
