import ctypes
# Test ctypes.CField.from_address()

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

x = X()
print x.a, x.b

p = pointer(x)

f = ctypes.CField.from_address(p, X, "a")
print f.offset, f.size
f.value = 42
print x.a, x.b

f = ctypes.CField.from_address(p, X, "b")
print f.offset, f.size
f.value = 43
print x.a, x.b
