import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double(2.0)

def f(p):
    p.x += 1
    p.y += 2
    return p

s = S()
print(s.x, s.y)

