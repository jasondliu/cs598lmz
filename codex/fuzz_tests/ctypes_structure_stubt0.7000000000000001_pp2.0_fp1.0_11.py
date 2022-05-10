import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    _fields_ = [
        ('y', x),
    ]

assert S.y is S.x
