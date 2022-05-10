import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

def p(num):
    print(ctypes.sizeof(num), struct.pack('dd', *num))

def pp(num):
    print(ctypes.sizeof(num), struct.pack('dd', *num[0]), struct.pack('dd', *num[1]))

def main():
    # p(2.0)
    # p(2)
    # p(2.0 + 2)
    # p(S(2.0, 2))
    # p(S(2, 2))

    p(S(2.0, 2))
    p(S(2, 2))
    # pp((S(2.0, 2), S(2, 2)))
    # pp((S(2, 2), S(2.0, 2)))

if __name__ == '__main__':
    main()
</code>
Notice how the struct.pack function gives the same results for S(2.0, 2) and S(2, 2). Why? Also
