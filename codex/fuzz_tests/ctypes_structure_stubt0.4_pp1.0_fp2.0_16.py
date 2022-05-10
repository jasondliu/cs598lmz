import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

class S2(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

class T(ctypes.Structure):
    _fields_ = [
        ("s", S),
        ("s2", S2),
    ]

t = T()
t.s.x = 1
t.s2.x = 2
print t.s.x, t.s2.x
