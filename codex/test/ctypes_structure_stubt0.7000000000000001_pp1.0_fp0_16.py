import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()

class U(ctypes.Union):
    x = ctypes.c_longdouble()
    y = ctypes.c_int()

