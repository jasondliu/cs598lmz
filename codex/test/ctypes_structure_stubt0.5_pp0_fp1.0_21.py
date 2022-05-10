import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x, y, z):
    s = S(x, y, z)
    return s.x + s.y + s.z

def g(n):
    return f(n, n+1, n+2)

def main(n):
    res = 0
    for i in range(n):
        res += g(i)
