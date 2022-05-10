import ctypes
# Test ctypes.CFUNCTYPE

def test_CFUNCTYPE():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = dll._testfunc_p_p
    func.argtypes = (ctypes.c_void_p,)
    func.restype = ctypes.c_void_p

    # call the function with a Python integer
    res = func(42)
    # the result should be a pointer to a copy of the integer
    assert ctypes.cast(res, ctypes.POINTER(ctypes.c_int))[0] == 42

    # call the function with a ctypes instance
    res = func(ctypes.c_int(42))
    # the result should be a pointer to a copy of the integer
    assert ctypes.cast(res, ctypes.POINTER(ctypes.c_int))[0] == 42

    # call the function with a ctypes instance
    res = func(ctypes.c_int())
    # the result should be a pointer to a copy of the integer
   
