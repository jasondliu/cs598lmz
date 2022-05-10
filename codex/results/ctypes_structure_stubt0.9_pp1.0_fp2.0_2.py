import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_long
    z = ctypes.c_ubyte


def main():
    s = S()
    s.x = 5
    s.y = 6
    s.z = 7
    ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s))
    print(s.x)
    print(s.y)
    print(s.z)
    
if __name__ == '__main__':
    main()
