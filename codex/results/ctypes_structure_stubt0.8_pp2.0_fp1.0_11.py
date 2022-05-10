import ctypes

class S(ctypes.Structure):
    x = 0
    _fields_ = [
        ('p', ctypes.c_void_p),
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ]

def main():
    s = S()
    print s.p
    s.p = ctypes.c_void_p(1)
    print s.p
    print s.x
    s.x = 11
    print s.x
    print s.y
    s.y = 22
    print s.y

if __name__ == '__main__':
    main()
