import ctypes

class S(ctypes.Structure):
    x = ctypes.c_size_t

def f(s):
    s.x = 1

def g():
    a = S()
    f(a)
    return a.x

def main():
    print(g())

main()
