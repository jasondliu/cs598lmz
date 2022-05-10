import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def cb(arg):
    print arg
    return 0

CALLBACK = FUNTYPE(cb)

def main():
    dll = ctypes.CDLL('./libfoo.so')
    dll.foo(CALLBACK)

if __name__ == '__main__':
    main()
