import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(5)
    y = ctypes.c_int(6)

