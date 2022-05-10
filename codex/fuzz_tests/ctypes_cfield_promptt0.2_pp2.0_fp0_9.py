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

y.x = X(4, 5)
print y.x.a, y.x.b, y.c

y.x = X(a=6, b=7)
print y.x.a, y.x.b, y.c

y.x = X(b=8, a=9)
print y.x.a, y.x.b, y.c

y.x = X(a=10)
print y.x.a, y.x.b, y.c

y.x = X(b=11
