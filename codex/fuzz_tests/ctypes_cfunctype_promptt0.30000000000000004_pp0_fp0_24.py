import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x):
    print "func", x
    return x * 2

CFUNCTYPE(c_int, c_int)(func)(42)

# Test ctypes.POINTER

from ctypes import *

class POINTER(object):
    def __init__(self, typ):
        self.typ = typ

    def from_param(self, param):
        typ = type(param)
        if typ is self.typ:
            return param
        if issubclass(typ, (Array, c_char_p, c_wchar_p)):
            return param
        if issubclass(typ, Structure):
            return param
        raise TypeError(
            "wrong type %s (expected %s or ctypes array of %s)" % (
                typ, self.typ, self.typ))

class X(Structure):
    _fields_ = [("a", c_int)]

p = POINTER(X)
x = X()
x.a = 42
assert p.from_param(
