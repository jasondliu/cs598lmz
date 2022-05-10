import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte

s = S()
s.x = 0xA5
s.y = 0x5A
