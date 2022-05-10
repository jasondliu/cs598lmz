import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
y.x.a = 1
y.x.b = 2
y.c = 3

print y.x.a, y.x.b, y.c

# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
y.x.a = 1
y.x.b = 2
y.c = 3

print y.x.a, y.x.
