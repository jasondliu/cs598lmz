import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint(0)
    y = ctypes.c_uint(1)

def f(s):
    return s.x

def g(s):
    return s.y

f(S()) # good
g(S()) # bad
