import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong(1)
    y = ctypes.c_ulong(2)

