import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f():
    return S()

def g():
    return f()

def h():
    return g()

def main():
    s = h()
    print s.x, s.y

main()
