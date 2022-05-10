import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S(x=1)

def f():
    s.x = 2
    g()

def g():
    pass



