import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

#

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int)]

class Z(Union):
    _fields_ = [("a", c_int),
                ("b", c_int)]

def func(a, b, c, d):
    return a, b, c, d

CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

def mycmp(a, b):
    return a - b

def test_functype():
    # simple function types
    f = CFUNCTYPE(c_int, c_int)(func)
    assert f(1, 2, 3, 4) == (1, 2, 3, 4)

    f = CFUNCTYPE(c_int, c_int, c_int, c
