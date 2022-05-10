import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    return x.x

def g(x):
    x.x = 1

def h(x):
    x.x = 1
    return x

def main():
    s = S()
    f(s)
    g(s)
    h(s)

main()
