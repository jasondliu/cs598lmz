import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("y", Y)]

z = Z()
z.a = 1
z.y.x.a = 2
z.y.x.b = 3

print z.a, z.y.x.a, z.y.x.b

print Z.a.offset, Z.y.offset, Z.y.x.offset

print Z.y.x.a.offset, Z.y.x.b.offset

assert Z.a.offset == 0
assert Z.y.offset == ctypes.sizeof(ctypes.c_int)
assert Z.y.x.offset == ctypes.sizeof(ctypes.c_int)
assert Z.y.x.a.
