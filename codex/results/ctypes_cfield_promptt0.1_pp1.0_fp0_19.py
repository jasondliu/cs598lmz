import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("d", ctypes.c_int)]

z = Z()
z.y.x.a = 1
z.y.x.b = 2
z.y.c = 3
z.d = 4

print z.y.x.a, z.y.x.b, z.y.c, z.d

print z.y.x.a == 1
print z.y.x.b == 2
print z.y.c == 3
print z.d == 4

print z.y.x.a == z.y.x.b
print z.y.x.a == z.y.c
print z.y.
