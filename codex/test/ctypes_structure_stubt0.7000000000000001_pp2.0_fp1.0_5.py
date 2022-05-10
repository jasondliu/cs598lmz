import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint

s = S()
s.x = 0x4040404040404040
