import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

z = Z()
z.y.x.a = 1
z.y.x.b = 2
z.y.y = 3
z.z = 4

print(z.y.x.a, z.y.x.b, z.y.y, z.z)

print(Z.y.x.a)

print(Z.y.x.b)

print(Z.y.y)

print(Z.z)

# Test ctypes.CFuncPtr
#
# XXX: This is not yet implemented, but it should be.
#
# from ctypes import
