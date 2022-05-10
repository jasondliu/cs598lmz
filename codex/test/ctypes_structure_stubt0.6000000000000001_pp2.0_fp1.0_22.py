import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(0)
    y = ctypes.c_long(0)

s = S()
print(s.x, s.y)
s.x = 100
s.y = 200
print(s.x, s.y)
