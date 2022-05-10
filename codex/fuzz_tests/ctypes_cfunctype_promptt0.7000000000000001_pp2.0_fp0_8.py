import ctypes
# Test ctypes.CFUNCTYPE.
from ctypes import *
from ctypes.test import need_symbol

class X(Structure):
    _fields_ = [("a", c_int)]

# XXX THIS IS BROKEN
##lib = CDLL(ctypes.util.find_library("c"))
##f = CFUNCTYPE(c_int, POINTER(X))(("setjmp", lib), ((1, "x"),))
##if f(pointer(X(1))).value != 1:
##    raise RuntimeError, "CFUNCTYPE"

# XXX THIS IS BROKEN
##f = CFUNCTYPE(c_int, c_int)
##lib = CDLL(ctypes.util.find_library("m"))
##lib.sin.restype = f
##if lib.sin(1).value != 1:
##    raise RuntimeError, "CFUNCTYPE"

# XXX THIS IS BROKEN
##f = CFUNCTYPE(c_int, c_int)
##lib = CDLL(ctypes.util.find_library
