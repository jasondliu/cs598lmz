import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1),
                ("b", ctypes.c_int, 2),
                ("c", ctypes.c_int, 3),
                ("d", ctypes.c_int, 4),
                ("e", ctypes.c_int, 5),
                ("f", ctypes.c_int, 6),
                ("g", ctypes.c_int, 7),
                ("h", ctypes.c_int, 8)]

c = C(1,2,3,4,5,6,7,8)
print c.a, c.b, c.c, c.d, c.e, c.f, c.g, c.h
c.a = 0
c.b = 0
c.c = 0
c.d = 0
c.e = 0
c.f = 0
c.g = 0
c.h = 0
print c.a, c.b, c.c, c.d, c.e, c.f
