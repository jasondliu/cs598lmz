import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def main():
    s = S()
    s.x = 1
    s.y = 2
    f(s)
    g(s)
    h(s)

main()
