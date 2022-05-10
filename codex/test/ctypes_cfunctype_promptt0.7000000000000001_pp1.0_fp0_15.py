import ctypes
# Test ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

class X(Exception):
    pass

def callback(arg):
    if arg == -1:
        raise X
    return arg * 2

import _ctypes_test

CallbackType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cb = CallbackType(callback)

# a normal call
res = cb(5)
