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
print z.y.x.a
print z.y.x.b
print z.y.c
print z.d

z.y.x.a = 1
z.y.x.b = 2
z.y.c = 3
z.d = 4

print z.y.x.a
print z.y.x.b
print z.y.c
print z.d

z.y.x = X(5, 6)
z.y = Y(X(7, 8), 9)
z = Z(Y(X(10, 11), 12),
