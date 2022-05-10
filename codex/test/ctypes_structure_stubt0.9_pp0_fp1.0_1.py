import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ('y', ctypes.c_float),
        ('z', ctypes.c_float),
        ('x', ctypes.c_float),
    ]
