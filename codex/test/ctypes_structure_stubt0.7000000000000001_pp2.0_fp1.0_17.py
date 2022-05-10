import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_uint
    z = ctypes.c_int64
    w = ctypes.c_uint64

