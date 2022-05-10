import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    y = ctypes.c_double(2.0)
