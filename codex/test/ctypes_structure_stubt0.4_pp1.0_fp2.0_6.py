import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    s = S()
    s.x = x
    return s

def g(x):
    s = f(x)
    return s.x

def main(n):
    for i in range(n):
        g(i)

main(100000)
