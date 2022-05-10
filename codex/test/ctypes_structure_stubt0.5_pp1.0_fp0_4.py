import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

def f():
    s = S()
    s.x = 3
    return s

def g():
    s = S()
    s.x = 4
    return s

def main():
    s1 = f()
    s2 = g()
