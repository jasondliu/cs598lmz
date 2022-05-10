import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()

class V(ctypes.Union):
    _fields_ = [
        ('arr', ctypes.c_double * 3),
        ('s', S)
    ]

