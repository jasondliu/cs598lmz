import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(x=1, y=2)

print(s.x)
print(s.y)
print(s.x + s.y)
