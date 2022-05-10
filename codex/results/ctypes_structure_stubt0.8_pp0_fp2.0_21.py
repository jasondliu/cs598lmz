import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int


def main():
    s = S()
    print(s.x)
    print(s.y)
    print(s.z)

    s.x = 1
    s.y = 2
    s.z = 3

    print(s.x)
    print(s.y)
    print(s.z)

    c_array = ctypes.c_int * 3
    s = ctypes.cast(c_array(1,2,3), ctypes.POINTER(S))

    print(s[0].x)
    print(s[0].y)
    print(s[0].z)

    print(s[1].x)
    print(s[1].y)
    print(s[1].z)

    print(s[2].x)
    print(s[2].y)
    print(s[2].z)


if __name__ == '__main__':
    main()
