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
z.y.x.a = 5
z.y.x.b = 6
z.y.y = 7
z.z = 8

print z.y.x.a
print z.y.x.b
print z.y.y
print z.z

print z.y.x.a == 5
print z.y.x.b == 6
print z.y.y == 7
print z.z == 8

print z.y.x.a == z.y.x.b
print z.y.x.a == z.y.y
print z
