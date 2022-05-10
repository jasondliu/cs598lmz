import ctypes
# Test ctypes.CFUNCTYPE()

# Test ctypes.CFUNCTYPE()

def test_cfunctype():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)

    # int func(int)
    FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    func = FUNC(("func_int_int", dll))
    assert func(42) == 42

    # int func(void)
    FUNC = ctypes.CFUNCTYPE(ctypes.c_int)
    func = FUNC(("func_void_int", dll))
    assert func() == 42

    # int func(char)
    FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char)
    func = FUNC(("func_char_int", dll))
    assert func(b'a') == 97

    # int func(char)
