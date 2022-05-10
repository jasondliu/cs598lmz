import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)
    return args[-1]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

_ctypes_test.set_callback(callback)

_ctypes_test.call_callback(1, 2)

# test that the callback is still alive
_ctypes_test.call_callback(3, 4)

# test that the callback is still alive
_ctypes_test.call_callback(5, 6)
