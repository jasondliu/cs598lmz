import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 42

s_p = ctypes.pointer(s)
