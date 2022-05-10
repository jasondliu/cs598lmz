import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

def F(S):
    return S.x * S.y

