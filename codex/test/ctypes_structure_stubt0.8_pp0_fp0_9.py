import ctypes

class S(ctypes.Structure):
    x = ctypes.c_size_t
    y = ctypes.c_size_t

def f(n):
    p = (S * n)()
    for i in range(n):
        p[i].x = i
        p[i].y = i
    s = 0
    for i in range(n):
        s += p[i].x + p[i].y
    return s

