import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
print y.a, y.b, y.c
y.a = 1
y.b = 2
y.c = 3
print y.a, y.b, y.c
print y.x.a, y.x.b, y.x.c
y.x.a = 4
y.x.b = 5
y.x.c = 6
print y.a, y.b, y.c
print y.x.a, y.x.b, y.x.c
print y.x.x.a, y.x.x.b, y.x.x.c
y.x.x.a = 7
y.x.x.b = 8
y.x.x.c = 9

