import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)
