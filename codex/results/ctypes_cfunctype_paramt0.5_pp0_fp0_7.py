import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_func(func):
    #print('func:', func)
    func.restype = ctypes.c_int
    func.argtypes = [ctypes.c_int]
    return func(1)

if __name__ == '__main__':
    lib = ctypes.CDLL('./libtest.so')
    func1 = lib.func1
    print(test_func(func1))
    print(test_func(FUNTYPE(func1)))
    func2 = lib.func2
    print(test_func(func2))
    print(test_func(FUNTYPE(func2)))
