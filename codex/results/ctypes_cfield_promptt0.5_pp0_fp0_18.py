import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_char)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_char)]

class Z(ctypes.Union):
    _fields_ = [("x", X),
                ("y", Y)]

z = Z()
z.x.a = b"A"
z.x.b = b"B"
z.x.c = b"C"

print(z.x.a, z.x.b, z.x.c)
print(z.y.a, z.y.b, z.y.c)

z.y.a = b"a"
z.y.b = b"b"
z.y.c = b"c"

print(z.x.
