import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

print(Z.y.x.a)
print(Z.y.x.b)
print(Z.z)

z = Z()
z.y.x.a = 1
z.y.x.b = 2
z.z = 3
print(z.y.x.a)
print(z.y.x.b)
print(z.z)

# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.
