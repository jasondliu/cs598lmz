import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(x):
    return x.x + x.y

def g(x):
    return x.x + x.y

def h(x):
    return x.x + x.y

def main():
    s = S()
    s.x = 1
    s.y = 2
    print f(s)
    print g(s)
    print h(s)

main()
