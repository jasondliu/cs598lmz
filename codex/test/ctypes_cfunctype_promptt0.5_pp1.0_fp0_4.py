import ctypes
# Test ctypes.CFUNCTYPE
#
# This test was written by Thomas Heller to find bugs in the
# ctypes.CFUNCTYPE implementation.

from ctypes import *

import _ctypes_test

dll = CDLL(_ctypes_test.__file__)

class X(Structure):
    _fields_ = [("x", c_int)]

class Y(Structure):
    _fields_ = [("y", c_int)]

Xp = POINTER(X)
Yp = POINTER(Y)

def check(restype, argtypes, func, params):
    cfunc = CFUNCTYPE(restype, *argtypes)(func)
    res = cfunc(*params)
    print(func.__name__, params, "->", res)
    return res

