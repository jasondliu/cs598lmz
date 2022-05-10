import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(p):
    p.contents.x = 1
    p.contents.y = 2

s = S()
f(ctypes.pointer(s))
print s.x, s.y
