import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32()
    y = ctypes.c_int32()

s = S()
s.x = 1
s.y = 2
