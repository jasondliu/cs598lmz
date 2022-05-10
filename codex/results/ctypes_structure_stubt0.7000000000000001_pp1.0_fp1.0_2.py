import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32
    z = ctypes.c_int32

def main():
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3

    print(s.x)
    print(s.y)
    print(s.z)

if __name__ == "__main__":
    main()
