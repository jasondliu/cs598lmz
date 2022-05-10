import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("I was called with %s and %s" % (a, b))
    return a + b

cbfunc = FUNTYPE(my_callback)

def main():
    mydll = ctypes.CDLL("mydll.dll")
    mydll.cfunc.argtypes = [ctypes.c_int, ctypes.c_int, FUNTYPE]
    mydll.cfunc.restype = ctypes.c_int
    result = mydll.cfunc(1, 2, cbfunc)
    print("mydll.cfunc returned %s" % result)

if __name__ == "__main__":
    main()
