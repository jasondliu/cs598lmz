import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong(0x12345678)

s = S()
s.x = 0x9abcdef0
print(s.x)
