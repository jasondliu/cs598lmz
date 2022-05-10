import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()

s = S()
s.x = 0xffffffff
print(s.x)
