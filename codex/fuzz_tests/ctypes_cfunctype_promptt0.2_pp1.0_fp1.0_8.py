import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function with a function pointer argument
def func(arg):
    print 'func', arg
    return arg

# call the function with a function pointer argument
lib.call_function(prototype(func), 1)

# call a function with a function pointer result

# prototype a function with a function pointer result
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function with a function pointer result
def func(arg):
    print 'func', arg
    return arg

# call the function with a function pointer result
lib.call_function(prototype(func), 1)

# call a function with a function pointer argument and result

# prototype a function with a function pointer argument and result
prototype
