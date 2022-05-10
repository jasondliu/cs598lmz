import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    a = ctypes.c_int
    b = ctypes.c_int
    c = ctypes.c_int
    d = ctypes.c_int
    e = ctypes.c_int
    f = ctypes.c_int
    g = ctypes.c_int
    h = ctypes.c_int
    i = ctypes.c_int

s = S()
s.x = 1
