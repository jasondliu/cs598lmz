import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", S)]

x = T()

x.a = 123
x.b = S()
x.b.x = 5
x.b.y = 5

