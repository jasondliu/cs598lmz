import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    b = ctypes.c_byte()


def main():
    s = S()
    TYPE_SIZE = ctypes.sizeof(s)
    print TYPE_SIZE
    s.b = 1
    print s.x

if __name__ == "__main__":
    main()
