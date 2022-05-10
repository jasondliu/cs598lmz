import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("e", D),
                ("f", ctypes.c_int)]

e = E()
e.e.c.a = 1
e.e.c.b = 2
e.e.d = 3
e.f = 4

print(e.e.c.a, e.e.c.b, e.e.d, e.f)

# Test ctypes.CField.in_dll

import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("
