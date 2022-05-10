import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype:
# int callback(int (*func)(int), int arg)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_callback(func):
    return func(1)

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_callbackfunc(func, arg):
    return func(arg)

# prototype:
# int callback_with_extra_args(int (*func)(int, int, int), int arg)
CALLBACK_WITH_EXTRA_ARGS = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

