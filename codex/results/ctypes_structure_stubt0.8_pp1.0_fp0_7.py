import ctypes

class S(ctypes.Structure):
    x = 2
    y = 3
    _fields_ = [
        ('y', ctypes.c_int),
        ('x', ctypes.c_int)]

print S().x
