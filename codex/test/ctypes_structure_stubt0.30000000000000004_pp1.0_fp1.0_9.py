import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    s = S()
    s.x = 1
    return s

def main():
    f()
    return 0

main()
