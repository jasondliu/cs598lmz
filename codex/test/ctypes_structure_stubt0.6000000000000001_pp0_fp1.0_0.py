import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_char),
        ("c", ctypes.c_int),
    ]

s = S()
s.a = 123
