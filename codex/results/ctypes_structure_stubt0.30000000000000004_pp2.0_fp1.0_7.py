import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x, y, z):
    s = S()
    s.x = x
    s.y = y
    s.z = z
    return s

def main():
    print f(1, 2, 3)

main()
