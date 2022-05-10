import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def get_sizeof(obj):
    return ctypes.sizeof(type(obj))

