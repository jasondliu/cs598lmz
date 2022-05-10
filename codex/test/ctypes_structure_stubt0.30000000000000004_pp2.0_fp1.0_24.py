import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(a):
    a.x = 1
    a.y = 2

s = S()
f(s)
