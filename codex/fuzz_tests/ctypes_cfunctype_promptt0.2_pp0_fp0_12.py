import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function
def func(arg):
    return arg + 42

# call the function
lib.call_function(prototype(func), 5)

# call a function with a function pointer result

# prototype a function with a function pointer result
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function
def func(arg):
    return arg + 42

# call the function
lib.call_function_result(5)

# call a function with a function pointer argument and result

# prototype a function with a function pointer argument and result
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function
def
