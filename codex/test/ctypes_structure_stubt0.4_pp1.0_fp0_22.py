import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(S):
    pass

