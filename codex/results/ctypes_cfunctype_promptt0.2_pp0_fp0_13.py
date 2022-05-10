import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# the function pointer type
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function
def func(arg):
    print 'func', arg
    return arg + 1

# the function pointer
func_p = FUNC(func)

# the function that takes the function pointer
lib.pass_func(func_p)

# call a function with a function pointer result

# the function pointer type
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function
def func(arg):
    print 'func', arg
    return arg + 1

# the function pointer
func_p = FUNC(func)

# the function that takes the function pointer
lib.pass_func(func_p)

# call a function with a function pointer result

# the function
