import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    def func(a, b):
        return a + b
    func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
    assert func_ptr(1, 2) == 3
    assert func_ptr(ctypes.c_int(1), ctypes.c_int(2)) == 3
    assert func_ptr(ctypes.c_int(1), 2) == 3
    assert func_ptr(1, ctypes.c_int(2)) == 3
    assert func_ptr(1, 2) == 3
    assert func_ptr(ctypes.c_int(1), ctypes.c_int(2)) == 3
    assert func_ptr(ctypes.c_int(1), 2) == 3
    assert func_ptr(1, ctypes.c_int(2)) == 3
    #
    def func(a, b):
        return a + b
    func_ptr = ctypes.CFUNCTYPE
