import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

s = S()

def f(x, y):
    s.x = x
    s.y = y
    return s

print f(1, 2)
</code>

