import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    y = ctypes.c_void_p

s = S()
s.x = s.y
