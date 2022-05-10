import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64
    y = ctypes.c_int64

s = S()
s.x = 0x7fffffffffffffff
