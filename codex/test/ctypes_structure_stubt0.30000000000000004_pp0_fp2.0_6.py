import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("a", S),
                ("b", S)]

t = T()
t.a.x = 1
t.a.y = 2
t.b.x = 3
t.b.y = 4

