import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# test calling a function with a callback
_ctypes_test.set_callback(CMPFUNC(func))
_ctypes_test.call_callback(1, 2)

# test calling a function with a callback using keyword arguments
_ctypes_test.set_callback(CMPFUNC(func), arg1=1)
_ctypes_test.call_callback(2, 3)

# test calling a function with a callback using keyword arguments and
# a restype
_ctypes_test.set_callback(CMPFUNC(func), arg1=1, restype=ctypes.c_int)
_ctypes_test.call_callback(2, 3)

# test calling a function with a callback using keyword arguments and
# a argtypes
_ctypes_test.set_callback(CMPFUNC(func
