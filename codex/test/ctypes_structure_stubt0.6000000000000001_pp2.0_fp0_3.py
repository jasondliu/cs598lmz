import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    z = ctypes.c_short
    w = ctypes.c_short

a = ctypes.c_int()
a = -1

s = S()
s.x = -1
s.y = -1
s.z = -1
s.w = -1

