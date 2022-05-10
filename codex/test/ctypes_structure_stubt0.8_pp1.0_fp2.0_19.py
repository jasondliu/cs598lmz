import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

def get_struct(x, y, z):
    return S(x, y, z)

