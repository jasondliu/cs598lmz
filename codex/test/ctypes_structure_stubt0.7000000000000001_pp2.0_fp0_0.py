import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int32()

