import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ("a", ctypes.c_int, 1),
        ("b", ctypes.c_int, 1),
        ("c", ctypes.c_int, 1),
        ("d", ctypes.c_int, 1),
    ]

