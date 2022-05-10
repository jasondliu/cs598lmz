import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('y', ctypes.c_long), ('z', ctypes.c_double)]

