import ctypes
# Test ctypes.CFUNCTYPE()
def test_cfunctype():
    try:
        from ctypes import CFUNCTYPE
    except ImportError:
        skip('ctypes not available')
    import _testcapi
    FUNC = CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    func = FUNC(_testcapi.int_return_arg)
    raises(OverflowError, func, -1)
    res = func(42)
    assert res == 42

def test_os_fdopen():
    import os
    try:
        os.fdopen(1)
    except AttributeError:
        skip("os.fdopen not available")
    raises(TypeError, os.fdopen, "a")
    raises(TypeError, os.fdopen, 1, "a")
    # Windows doesn't support os.fdopen(fd, mode, bufsize)
    if hasattr(os, 'O_RDONLY'):
        fd = os.open(__file__, os.O_RDONLY)
