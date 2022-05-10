import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

p = S()
p.x = 5
p.y = 6
print(p.x)
print(p.y)
