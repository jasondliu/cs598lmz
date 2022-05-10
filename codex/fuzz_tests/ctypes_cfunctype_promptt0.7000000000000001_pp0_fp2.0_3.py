import ctypes
# Test ctypes.CFUNCTYPE(None)
if __name__ == '__main__':
    import _ctypes_test
    functype = ctypes.CFUNCTYPE(None)
    x = functype(lambda: None)
    #x(0)
    #_ctypes_test.func(x, 0)
    #_ctypes_test.func(x, 1)
    #_ctypes_test.func(x, 2)
    _ctypes_test.func(x, 3)
    #_ctypes_test.func(x, 4)
    #_ctypes_test.func(x, 5)
    #_ctypes_test.func(x, 6)
    #_ctypes_test.func(x, 7)
    #x(8)
    #_ctypes_test.func(x, 9)
    #_ctypes_test.func(x, 10)
