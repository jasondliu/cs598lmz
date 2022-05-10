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

check_type(CALLFUNCTYPE)

# The following types are accepted as well, because they are
# subclasses of CFUNCTYPE

class X(CALLFUNCTYPE):
    pass

check_type(X)

class Y(ctypes.Structure):
    _fields_ = [("func", CALLFUNCTYPE)]

check_type(Y.func
