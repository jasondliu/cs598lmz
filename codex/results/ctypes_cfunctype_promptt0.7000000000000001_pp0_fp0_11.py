import ctypes
# Test ctypes.CFUNCTYPE and ctypes.byref

def test_CFUNCTYPE():
    from ctypes import c_int
    from _ctypes import PyObj_FromPtr

    def func(arg):
        print(arg)

    FUNC = ctypes.CFUNCTYPE(c_int, c_int)
    cfunc = FUNC(func)
    x = cfunc(42)
    assert x == 42
    assert PyObj_FromPtr(cfunc) is func
    assert PyObj_FromPtr(func) is func

    # Ensure that a CFUNCTYPE with more than one parameter doesn't
    # cause a segfault in the byref() call.
    FUNC = ctypes.CFUNCTYPE(c_int, c_int, c_int)
    cfunc = FUNC(func)
    x = cfunc(42, 43)
    assert x == 42
    assert PyObj_FromPtr(cfunc) is func
    assert PyObj_FromPtr(func) is func

def test_byref():
    import _ctypes
   
