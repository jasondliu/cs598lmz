import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

s = S()
