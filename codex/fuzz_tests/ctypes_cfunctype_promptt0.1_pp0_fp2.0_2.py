import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a function with a function pointer argument
def func(arg):
    return arg + 42

# call the function with the function pointer
res = lib.call_function(prototype(func), 5)
if res != 47:
    raise RuntimeError("function call failed")

# call a function with a function pointer argument
# and a user defined data pointer

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

# define a function with a function pointer argument
def func(arg, data):
    return arg + ctypes.cast(data, ctypes.POINTER(ctypes.c_int))[0]

# call
