import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    x.x = 5

s = S()
