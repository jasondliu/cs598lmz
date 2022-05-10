import ctypes
# Test ctypes.CFUNCTYPE by creating a callback that gets an integer argument
# and returns a c_char_p.  This is used in the callback tests.
def _test_cfunc(n):
    return ctypes.c_char_p(b"hello %d" % n)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)

# Callback types
CFUNCTYPE = ctypes.CFUNCTYPE
