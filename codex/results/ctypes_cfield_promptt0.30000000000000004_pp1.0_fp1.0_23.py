import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", Y)]

z = Z()
z.y.x.a = 1
z.y.x.b = 2
z.y.y.a = 3
z.y.y.b = 4
z.z.y.a = 5
z.z.y.b = 6
z.z.z.a = 7
z.z.z.b = 8

print z.y.x.a, z.y.x.b
print z.y.y.a, z.y.y.b
print z.z.y.a, z.z.y.b
print z.z.z.a, z.z.z.b


