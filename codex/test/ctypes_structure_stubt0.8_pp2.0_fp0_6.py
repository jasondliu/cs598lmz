import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class S2(S):
    y = ctypes.c_int

class S3(S2):
    z = ctypes.c_int()

