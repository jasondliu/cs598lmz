import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte()
    y = ctypes.c_byte()
    z = ctypes.c_byte()

s = S()
s.x = 1
s.y = 2
s.z = 3

