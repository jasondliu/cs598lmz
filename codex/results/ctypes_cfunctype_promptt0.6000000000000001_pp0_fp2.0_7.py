import ctypes
# Test ctypes.CFUNCTYPE
#
# To ensure that this compiles, we need to make sure that we don't
# default to stdcall on a platform that supports stdcall.
def test_CFUNCTYPE():
    from ctypes import CFUNCTYPE, c_int

    has_argtypes = hasattr(CFUNCTYPE, 'argtypes')
    if has_argtypes:
        PyCFuncPtr = CFUNCTYPE(c_int, c_int)
    else:
        PyCFuncPtr = CFUNCTYPE(c_int)

    if sys.platform == "win32":
        from ctypes import WINFUNCTYPE
        PyWinFuncPtr = WINFUNCTYPE(c_int, c_int)
        f = PyWinFuncPtr(lambda x: x)
    else:
        f = PyCFuncPtr(lambda x: x)
    assert f(42) == 42
    assert f.__call__(42) == 42

    # calling the CFUNCTYPE instance should fail
    raises(TypeError, f)

def test_
