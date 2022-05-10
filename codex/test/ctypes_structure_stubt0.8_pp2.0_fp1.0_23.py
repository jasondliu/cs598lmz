import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.0)
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("next", ctypes.POINTER(ctypes.c_double))
    ]

s = S()
s.y = 1.0
