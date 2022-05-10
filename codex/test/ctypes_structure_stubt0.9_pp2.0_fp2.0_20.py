import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class U(ctypes.Union):
    y = ctypes.c_int
    x = S    # invalid indirection

