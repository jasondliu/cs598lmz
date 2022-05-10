import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    s = S()
    s.x = 5
    return s

def main():
    s = f()
    print(s.x)

main()
