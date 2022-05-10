import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(s):
    s.x = 1
    s.y = 2

s = S()
f(s)
