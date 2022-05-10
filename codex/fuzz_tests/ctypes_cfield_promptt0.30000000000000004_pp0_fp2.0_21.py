import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
y.x.a = 1
y.x.b = 2
y.c = 3

print y.x.a, y.x.b, y.c

y.x.a = 4
y.x.b = 5
y.c = 6

print y.x.a, y.x.b, y.c

# Test ctypes.CArray

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int * 3),
                ("b", ctypes.c_int)]

z = Z()
z.a[0] = 1
z.a[1] = 2
z.a[2] = 3
z.b = 4

print z
