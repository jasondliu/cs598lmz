import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    return x

def g(x):
    return x

def main():
    a = S()
    a.x = 1
    f(a)
    g(a)

main()
