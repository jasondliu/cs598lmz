import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a function with a function pointer argument
def func(arg):
    return arg

# call the function with the function pointer
lib.pass_func(prototype(func))

# call a function with a function pointer argument
# and a user defined data pointer

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

# define a function with a function pointer argument
def func(arg, data):
    return arg + ctypes.cast(data, ctypes.POINTER(ctypes.c_int))[0]

# call the function with the function pointer
lib.pass_func_userdata(prototype(func), ctypes
