import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

def f(x, y):
    s = S()
    s.x = x
    s.y = y
    s.x = s.x + s.y
    return s.x

print(f(1, 2))
