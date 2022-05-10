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

