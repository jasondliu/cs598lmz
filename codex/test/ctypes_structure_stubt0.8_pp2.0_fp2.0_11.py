import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    y = ctypes.c_float(2.0)
    z = ctypes.c_float(3.0)

