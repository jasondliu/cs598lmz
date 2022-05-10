import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64()
    y = ctypes.c_uint64()

class L(ctypes.Structure):
    size = ctypes.c_uint16()
