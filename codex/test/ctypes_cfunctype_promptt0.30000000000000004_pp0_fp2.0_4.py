import ctypes
# Test ctypes.CFUNCTYPE(None)
def test_CFUNCTYPE_None():
    import _ctypes_test
    lib = ctypes.CDLL(_ctypes_test.__file__)
    func = ctypes.CFUNCTYPE(None)(("test_func_0", lib), ())
    func()

# Test ctypes.CFUNCTYPE(ctypes.c_int)
def test_CFUNCTYPE_c_int():
    import _ctypes_test
    lib = ctypes.CDLL(_ctypes_test.__file__)
    func = ctypes.CFUNCTYPE(ctypes.c_int)(("test_func_1", lib), (ctypes.c_int,))
    assert func(1) == 1

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def test_CFUNCTYPE_c_int_c_int():
    import _ctypes_test
    lib = ctypes.CDLL(_ctypes_test.__file__)
