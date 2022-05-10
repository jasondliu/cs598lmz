import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("y", Y)]

# This is a bug in Python 2.4.3, it should not be necessary to
# explicitly initialize the fields.
y = Y()
y.a = 1
y.b = 2
y.x.a = 3
y.x.b = 4

z = Z()
z.a = 1
z.b = 2
z.y.a = 3
z.y.b = 4
z.y.x.a = 5
z.y.x.b = 6

print(z.a
