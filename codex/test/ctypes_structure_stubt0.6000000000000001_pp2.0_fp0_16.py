import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class U(ctypes.Union):
    x = ctypes.c_int
    y = ctypes.c_int

