import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ushort(123)

s = S()
s2 = S.from_buffer(bytearray(s))
print(s2.x)
