import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(s):
    s.x = 10
    s.y = 20

s = S()
f(s)
print(s.x, s.y)
