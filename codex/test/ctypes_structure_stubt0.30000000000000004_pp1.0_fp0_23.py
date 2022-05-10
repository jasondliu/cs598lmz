import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    s = S()
    s.x = 1
    return s

def g():
    return f()

def h():
    return g()

def main():
    s = h()
