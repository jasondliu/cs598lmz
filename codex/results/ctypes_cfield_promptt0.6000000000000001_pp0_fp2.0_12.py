import ctypes
# Test ctypes.CField() and ctypes.CData()
import sys
from ctypes import *
from ctypes.test import need_symbol

libm = CDLL(ctypes.util.find_library("m"))

class X(Union):
    _fields_ = [("p", c_void_p),
                ("i", c_int)]

class Y(Structure):
    _fields_ = [("x", X),
                ("d", c_double)]

y = Y()

# The following doesn't work for 64-bit platforms.
# libm.sin.restype = Y

if sizeof(c_long) == sizeof(c_void_p):
    libm.sin.restype = c_long
else:
    libm.sin.restype = c_int

y = libm.sin(0)
if sizeof(c_long) == sizeof(c_void_p):
    assert type(y) is int
    assert y == 0
else:
    assert type(y) is int
    assert y == 0


libm.sin.restype
