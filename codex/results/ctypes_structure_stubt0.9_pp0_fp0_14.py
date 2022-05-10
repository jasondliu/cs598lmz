import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    pass


print ctypes._endian
