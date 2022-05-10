import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(42)
    y = ctypes.c_float(123)
