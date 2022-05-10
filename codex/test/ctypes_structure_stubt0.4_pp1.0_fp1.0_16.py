import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(S):
    x = ctypes.c_short

ctypes.sizeof(D)
