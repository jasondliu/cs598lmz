import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def main():
    a = S()
    b = S()
    a.x = 1
    a.y = 2
    a.z = 3
    b.x = 1
    b.y = 2
    b.z = 4

    print a == b
    print a != b

if __name__ == "__main__":
    main()
