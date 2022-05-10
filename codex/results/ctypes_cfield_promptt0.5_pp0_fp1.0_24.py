import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

z = Z()
z.y.x.a = 1
z.y.x.b = 2
print z.y.x.a, z.y.x.b

# Test ctypes.CArray
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X * 2)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

z = Z()
z.y.x[0].a = 1
z.y.x[0].b = 2
z
