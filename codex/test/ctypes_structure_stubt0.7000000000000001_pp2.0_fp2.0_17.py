import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16
    y = ctypes.c_uint16

s = S()
s.x = 0x12345678
s.y = 0xabcdef12

