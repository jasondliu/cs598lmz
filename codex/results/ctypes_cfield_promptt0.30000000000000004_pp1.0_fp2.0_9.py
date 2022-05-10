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
z.y.x.a = 42
z.y.x.b = 43
z.y.y = 44
z.z = 45

print z.y.x.a, z.y.x.b, z.y.y, z.z

print z.y.x.a, z.y.x.b, z.y.y, z.z

print z.y.x.a, z.y.x.b, z.y.y, z.z

print z.y.x.a, z.y.x.b, z.y
