import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    z = ctypes.c_double()
    _fields_ = [
        ("x", ctypes.c_double),
        ("z", ctypes.c_double)
    ]

