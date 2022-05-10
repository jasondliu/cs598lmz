import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

f = S()
f.x = 1
f.y = 10
print(f.x, f.y)
