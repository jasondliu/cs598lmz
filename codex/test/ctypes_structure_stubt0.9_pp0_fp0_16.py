import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8

s = S()
s.x = 0x10
s.y = 0x16
