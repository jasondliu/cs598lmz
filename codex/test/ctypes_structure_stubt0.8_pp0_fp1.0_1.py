import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_double
    z = ctypes.c_short
    i = ctypes.c_int
    j = ctypes.c_int

