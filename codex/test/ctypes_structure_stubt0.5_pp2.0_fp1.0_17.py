import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8
    z = ctypes.c_uint8

s = S()
s.x = 0x12
s.y = 0x34
s.z = 0x56

print(s.x, s.y, s.z)
