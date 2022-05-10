import ctypes

class S(ctypes.Structure):
    x = 2
    y = 3
    _fields_ = [
        ('x', ctypes.c_byte),
        ('y', ctypes.c_byte),
        ('z', ctypes.c_byte),
        ('w', ctypes.c_byte),
    ]

s = S()
