import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class S2(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def main():
    s = S()
    s.x = 1
    s.y = 2

    s2 = S2()
    s2.x = 1
    s2.y = 2
    s2.z = 3

    print s.x, s.y
    print s2.x, s2.y, s2.z

if __name__ == '__main__':
    main()
