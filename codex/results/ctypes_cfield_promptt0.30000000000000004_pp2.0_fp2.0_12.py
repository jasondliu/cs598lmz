import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

print Y.x.a
print Y.x.b
print Y.c

# Test ctypes.CField.from_address

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
print Y.x.from_address(ctypes.addressof(y))
print Y.x.from_address(ctypes.addressof(y)).a
print Y.x.from_address(ctypes.addressof(y
