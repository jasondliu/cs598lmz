import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This function takes a function pointer as argument, and calls
# the function.

def callback(result, func, args):
    func(args)
    return 0

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                            ctypes.c_void_p, ctypes.py_object)

lib = ctypes.CDLL(ctypes.util.find_library("c"))
lib.test_callback.argtypes = (CALLBACK, ctypes.c_int, ctypes.py_object)

def func(args):
    print("called back with", args)

lib.test_callback(CALLBACK(callback), 42, func)
