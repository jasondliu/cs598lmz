import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# XXX This is not a complete test, but it's a start.

def test_CFUNCTYPE():
    if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
        c_ssize_t = ctypes.c_long
    else:
        c_ssize_t = ctypes.c_int

    # XXX This is not a complete test, but it's a start.
    c_ssize_p = ctypes.POINTER(c_ssize_t)
    c_ssize_pp = ctypes.POINTER(c_ssize_p)

    def func(*args):
        return args

    CFunc = ctypes.CFUNCTYPE(c_ssize_t, c_ssize_t, c_ssize_p, c_ssize_pp)
    cfunc = CFunc(func)
    assert cfunc(1, (2,), ((3,),)) == (1, (2,), ((3,),))


