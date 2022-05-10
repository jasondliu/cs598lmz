import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class X(ctypes.Structure):
    _fields_ = [
        ("a", S),
        ("b", S),
        ("c", ctypes.c_int),
    ]

x = X()
print(x.a.x)
