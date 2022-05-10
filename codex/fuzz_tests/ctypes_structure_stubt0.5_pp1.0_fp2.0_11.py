import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def g(x, y):
    return x + y

s = S()
s.x = 1
s.y = 2

print(g(s.x, s.y))
