import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x):
    s = S()
    s.x = x
    s.y = x + 1
    s.z = x + 2
    return s

def main():
    print(f(1))

main()
