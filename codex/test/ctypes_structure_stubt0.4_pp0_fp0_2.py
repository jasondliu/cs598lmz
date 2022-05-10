import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(s):
    s.x = 123
    s.y = 456

s = S()
f(s)
print(s.x, s.y)
