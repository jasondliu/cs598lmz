import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f():
    s = S()
    s.x = 1
    s.y = 2
    return s

def g():
    s = S()
    s.x = 3
    s.y = 4
    return s

def main():
    s1 = f()
    s2 = g()
    print s1.x, s1.y
    print s2.x, s2.y

main()
