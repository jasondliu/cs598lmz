import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_float()
    z = ctypes.c_char()

