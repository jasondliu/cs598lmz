import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16()
    y = ctypes.c_uint16()

class T(ctypes.Structure):
    x = ctypes.c_uint16()
    y = ctypes.c_uint32()

s = S()
s.x = 0x1234
s.y = 0x5678

print(s.x, s.y)
