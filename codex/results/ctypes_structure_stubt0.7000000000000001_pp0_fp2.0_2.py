import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    z = ctypes.c_int
    a = ctypes.c_int

class X(ctypes.Union):
    _fields_ = [("s", S), ("t", T)]

x = X()

x.s.x = 1
x.s.y = 2
print x.s.x, x.s.y, x.t.z, x.t.a

x.t.z = 3
x.t.a = 4
print x.s.x, x.s.y, x.t.z, x.t.a
