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
if res != 10:
    print 'normal call failed:', res

# this raises X, which should be translated into a Python exception
try:
    res = cb(-1)
except X:
    pass
else:
    print 'exception not propagated:', res

# calling a callback from the C level which returns -1, should raise
# an exception, because use_errno is False
try:
    res = _ctypes_test.call_callback(cb, -1)
except ValueError:
    pass
else:
    print 'exception not propagated:
