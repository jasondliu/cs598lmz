import ctypes
# Test ctypes.CField.from_address
from ctypes import *
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("x", X),
                ("y", c_int)]

class Z(Structure):
    _fields_ = [("y", Y),
                ("z", c_int)]

p = c_void_p.in_dll(lib, "p")
assert p.value == 0

p.value = ctypes.addressof(lib.x)
assert p.value == ctypes.addressof(lib.x)

x = X.from_address(p.value)
assert x.a == 1
assert x.b == 2

p.value = ctypes.addressof(lib.y)
assert p.value == ctypes.addressof(lib.y)

y = Y.from_address(p.
