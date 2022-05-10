import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function takes a function pointer as first argument,
# and an integer as second argument.  The function is called
# with the integer as argument, and the function returns the
# integer.

CALLFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def check_type(tp):
    func = tp(lambda x: x)
    res = lib.call_function(func, 42)
    if res != 42:
        raise Exception("%s failed" % tp)

