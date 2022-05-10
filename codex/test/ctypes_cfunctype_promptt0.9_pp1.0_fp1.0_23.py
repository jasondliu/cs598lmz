import ctypes
# Test ctypes.CFUNCTYPE.
def test_cfunctype_issue5646():
    # First, test that we can create C functions using
    # ctypes.CFUNCTYPE.
    clib = cdll.msvcrt
    testfunctype = ctypes.CFUNCTYPE(ctypes.c_int)
    cfunc = testfunctype()
    code = ctypes.cast(lib.myfunction, ctypes.c_void_p).value
    try:
        cfunc.__code__.co_code == struct.pack('P', code)
    except AttributeError:
        try:
            cfunc.func_code.co_code == struct.pack('P', code)
        except AttributeError:
            pass
    if platform.machine().startswith('x86_64'):
        assert cfunc.func_globals is not None
        assert cfunc.func_closure is None
        assert cfunc.func_code.co_varnames is None
        assert cfunc.func_code.co_argcount == 0
        assert cfunc
