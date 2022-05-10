import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64()
    y = ctypes.c_int64()

