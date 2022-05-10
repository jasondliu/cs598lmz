import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def main():
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
    print(s.x, s.y, s.z)

if __name__ == '__main__':
    main()
