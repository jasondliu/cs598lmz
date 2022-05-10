import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

y = Y()
y.x.a = 42
y.x.b = 43
print y.x.a, y.x.b
