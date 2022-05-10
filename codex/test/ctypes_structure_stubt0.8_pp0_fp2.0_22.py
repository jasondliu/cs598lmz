import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_void_p
    z = ctypes.c_int

s = S()
s.x = 42
s.z = 3
