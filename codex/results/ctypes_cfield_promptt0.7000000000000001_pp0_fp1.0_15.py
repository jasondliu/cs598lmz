import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

x = D()

print x.a
print x.b
print x.c
