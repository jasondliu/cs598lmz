import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(S):
    pass

class E(S):
    y = ctypes.c_int

class F(D, E):
    pass

