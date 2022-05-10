import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def main():
    x = S()
    y = S()
    f(x)
    f(y)
    g(x)
    h(y)

main()
