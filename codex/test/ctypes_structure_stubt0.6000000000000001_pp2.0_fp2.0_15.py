import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    _fields_ = [
        ("y", ctypes.c_char),
        ("x", ctypes.c_char),
        ("z", ctypes.c_char),
    ]

s = S()
