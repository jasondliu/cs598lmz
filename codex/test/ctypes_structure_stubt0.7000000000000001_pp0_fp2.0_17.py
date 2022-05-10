import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_char()
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_char)
    ]

s = S()
