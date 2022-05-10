import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x, y, z):
    return x + y + z

f.restype = S

