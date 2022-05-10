import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER
from ctypes import *
from ctypes.test import need_symbol
import _ctypes_test

if sizeof(c_int) == sizeof(c_void_p):
    c_ptrdiff_t = c_int
else:
    c_ptrdiff_t = c_long

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int),
                ("d", c_int)]

if sizeof(c_int) == 4:
    class W(Structure):
        _fields_ = [("a", c_int),
                    ("b", c_int),
                    ("c", c_int),
                    ("d", c
