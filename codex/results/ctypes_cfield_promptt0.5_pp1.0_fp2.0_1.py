import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
y.x.a = 42
y.x.b = 24
y.c = 17

print y.x.a, y.x.b, y.c

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("d", ctypes.c_int)]

z = Z()
z.y.x.a = 42
z.y.x.b = 24
z.y.c = 17
z.d = -1

print z.y.x.a, z.y.x.b, z.y.c, z.d
