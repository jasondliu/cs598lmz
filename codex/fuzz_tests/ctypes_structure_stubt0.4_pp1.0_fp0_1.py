import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]

def main():
    s = S()
    print s.x
    s.x = 42
    print s.x

if __name__ == '__main__':
    main()
