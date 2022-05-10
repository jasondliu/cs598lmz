import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function prototype
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function
def func(arg):
    return arg + 42

# convert the function to a callable thing
func_c = prototype(func)

# call the function
res = lib.call_function(func_c, 1)
if res != 43:
    raise RuntimeError("%d != 43" % res)

# a function prototype
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# a function
def func(arg1, arg2):
    return arg1 + arg2

# convert the function to a callable thing
func_c = prototype(func)

# call the function
res = lib.call_function(func_c, 1, 2)
if res != 3:
    raise RuntimeError("%
