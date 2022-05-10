import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the signature:
# int func(int)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CALLBACK
def callback(arg):
    print("callback called with", arg)
    return arg + 1

lib.set_callback(callback)

print(lib.call_callback(5))

# This is a function that takes a function pointer as argument.
# The function pointer must have the signature:
# int func(int, void *)
CALLBACK2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

@CALLBACK2
def callback2(arg, data):
    print("callback2 called with", arg, data)
    return arg + 1

lib.set_callback2(callback2
