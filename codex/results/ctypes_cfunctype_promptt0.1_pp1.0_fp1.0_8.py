import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

# the function pointer type is defined in _ctypes_test
# it takes an int argument and returns an int
CALLFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function to be called takes a function pointer and an int argument
# and calls the function pointer with the int argument
lib.call_function.argtypes = (CALLFUNC, ctypes.c_int)
lib.call_function.restype = ctypes.c_int

# the Python callable
def func(arg):
    print("func", arg)
    return arg * 2

# call lib.call_function(func, 3)
res = lib.call_function(CALLFUNC(func), 3)
print("result", res)

# call a function with a function pointer argument
# the function pointer argument is a
