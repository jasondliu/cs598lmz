import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(a, b):
    return a + b

def main():
    func = FUNTYPE(add)
    print(func(1, 2))

if __name__ == '__main__':
    main()
