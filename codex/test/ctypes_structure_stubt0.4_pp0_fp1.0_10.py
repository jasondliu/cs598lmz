import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(x):
    print(x)
    x.x = 1
    x.y = 2

s = S()
f(s)
print(s.x, s.y)
