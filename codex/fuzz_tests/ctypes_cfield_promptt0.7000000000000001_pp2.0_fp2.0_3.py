import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", C)]

d = D()
f = ctypes.Field(d, "c", C)
print(f)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

f = ctypes.Field(X, "c", ctypes.c_int)
print(f)

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

f = ctypes.Field(Y, "c", ctypes.c_int)
print(f)

class Z(
