import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def add(x):
    return x+1

def sub(x):
    return x-1

def main():
    lib = ctypes.CDLL('./libtest.so')
    lib.set_callback(FUNTYPE(add))
    print(lib.use_callback(1))
    lib.set_callback(FUNTYPE(sub))
    print(lib.use_callback(1))

if __name__ == '__main__':
    main()
