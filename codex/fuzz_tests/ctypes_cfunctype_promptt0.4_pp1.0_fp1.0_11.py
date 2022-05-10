import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a CFUNCTYPE argument

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@prototype
def func(value):
    return value + 1

result = lib.call_function(func, 1)
if result != 2:
    raise Exception("Wrong result")

# call a function with a CFUNCTYPE argument, the function has a
# prototype defined

@prototype
def func(value):
    "func()"
    return value + 1

result = lib.call_function(func, 1)
if result != 2:
    raise Exception("Wrong result")

# call a function with a CFUNCTYPE argument, the function has a
# docstring

@prototype
def func(value):
    "func()"
    return value + 1

result = lib.call_function(func, 1)
if result != 2:
    raise
