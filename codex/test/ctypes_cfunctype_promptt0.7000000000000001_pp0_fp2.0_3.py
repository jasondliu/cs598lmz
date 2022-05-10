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
