import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()
    y = ctypes.c_double()
    z = ctypes.c_double()

