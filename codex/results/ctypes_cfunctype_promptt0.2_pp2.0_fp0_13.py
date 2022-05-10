import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function pointer type the CALLBACK function
# expects.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def addressof(cdata):
    return ctypes.addressof(ctypes.c_int.from_address(id(cdata)))

def callback(arg):
    print("callback called with", arg)
    return arg + 1

# This is the function to call.
func = FUNC(callback)

# This is the function that takes the function pointer.
# The argtypes list is not required, but serves as a
# check that the argument has the required type.
lib.pass_func.argtypes = (CALLBACK,)
lib.pass_func
