import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32(1)
    y = x
