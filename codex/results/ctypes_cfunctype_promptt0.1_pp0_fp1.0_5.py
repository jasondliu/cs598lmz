import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that is called by the function pointer.
def callback(arg):
    print("callback called with arg:", arg)
    return arg + 1

# This is the function that takes a function pointer as argument.
lib.call_function.argtypes = (CALLBACK,)
lib.call_function.restype = ctypes.c_int

# Call the function with the function pointer.
res = lib.call_function(CALLBACK(callback))
print("call_function returned:", res)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

#
