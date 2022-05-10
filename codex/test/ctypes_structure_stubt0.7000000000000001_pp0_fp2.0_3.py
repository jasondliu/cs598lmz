import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

    # This is optional
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

class T(ctypes.Structure):
    _fields_ = [
        ('a', S * 2)
    ]

a = S(1, 2)
b = S(3, 4)
t = T((a, b))
