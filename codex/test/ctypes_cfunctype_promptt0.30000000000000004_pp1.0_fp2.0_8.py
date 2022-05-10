import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    c_int_p = ctypes.POINTER(ctypes.c_int)
    c_int_p_p = ctypes.POINTER(c_int_p)
    def func(a, b):
        return a + b
    func_p = ctypes.CFUNCTYPE(ctypes.c_int, c_int_p, c_int_p)(func)
    assert func_p(c_int_p(42), c_int_p(24)) == 42 + 24
    assert func_p(c_int_p(42), c_int_p_p(c_int_p(24))) == 42 + 24
    assert func_p(c_int_p_p(c_int_p(42)), c_int_p(24)) == 42 + 24
    assert func_p(c_int_p_p(c_int_p(42)), c_int_p_p(c_int_p(24))) == 42 + 24
