import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class P(ctypes.Structure):
    _fields_ = [('b', ctypes.c_byte), ('a', ctypes.c_char_p)]

def main():
    s = S()
    print s.x
    s.x = 3
    print s.x

    p = P()
    print p.b
    print p.a
    p.b = 4
    p.a = 'foo'
    print p.b
    print p.a

if __name__ == '__main__':
    main()
