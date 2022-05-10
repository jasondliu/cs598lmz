import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    s = S()
    s.x = 1
    print s.x
    print type(s.x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
