import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(num):
    print("callback called with", num)
    return num * 2

def main():
    lib = ctypes.CDLL("./libtest.so")
    lib.test.argtypes = [FUNTYPE]
    lib.test.restype = ctypes.c_int

    cb = FUNTYPE(callback)
    res = lib.test(cb)
    print("test returned", res)

if __name__ == "__main__":
    main()
