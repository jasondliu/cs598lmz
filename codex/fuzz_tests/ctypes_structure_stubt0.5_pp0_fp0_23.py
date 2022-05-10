import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    return S()

def g():
    return f()

def main(n):
    for i in xrange(n):
        f()
    for i in xrange(n):
        g()

main(100000)
