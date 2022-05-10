import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

y = Y()
print y.x.a, y.x.b
print ctypes.c_int.in_dll(y, "x.a")
print ctypes.c_int.in_dll(y, "x.b")
print ctypes.c_int.in_dll(y, "y")

y.x.a = 2
y.x.b = 3
print y.x.a, y.x.b
print ctypes.c_int.in_dll(y, "x.a")
print ctypes.c_int.in_dll(y, "x.b")
print ctypes.c_int.in_dll(y, "y")

ctypes.c_int.in_dll(y, "
