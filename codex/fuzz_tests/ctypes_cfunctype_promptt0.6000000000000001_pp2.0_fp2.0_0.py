import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print "callback", arg
    return arg

CALLBACK = functype(callback)

_ctypes_test.set_callback(CALLBACK)

for i in range(5):
    print _ctypes_test.callbackfunc(i)
