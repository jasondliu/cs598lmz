import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double

class C(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_double)
    ]

