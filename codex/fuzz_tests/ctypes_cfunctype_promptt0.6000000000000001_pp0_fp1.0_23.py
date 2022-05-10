import ctypes
# Test ctypes.CFUNCTYPE

if sys.platform == 'win32':
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    # XXX We'd like to use stdcall instead of cdecl, but that leads to a crash
    # in the test_callbacks test.
    CallFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)
    func = CallFunc(("testfunc_cdecl", dll), ((1,), (1.0,)))
    assert func(3.14) == 42
    # XXX This crashes python.exe:
    #func = CallFunc(("testfunc_stdcall", dll), ((1,), (1.0,)))
    #assert func(3.14) == 42
    del func, CallFunc
    #
    # test calling a function from a different dll
    CallFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)
    func = CallFunc(("testfunc_
