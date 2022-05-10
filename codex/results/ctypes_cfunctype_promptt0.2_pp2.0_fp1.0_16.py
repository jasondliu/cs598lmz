import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument.
# The function pointer must have the same calling convention as
# the function that takes it.

# The prototype of the function is:
# void func(int(*callback)(int))

CALLBACK = CFUNCTYPE(c_int, c_int)

def callback(value):
    print('callback called with value', value)
    return value + 1

func = lib.func
func.argtypes = [CALLBACK]

func(CALLBACK(callback))

# Test ctypes.WINFUNCTYPE

# This is a function that takes a function pointer as an argument.
# The function pointer must have the same calling convention as
# the function that takes it.

# The prototype of the function is:
# void func(int(*callback)(int))

CALLBACK = WINFUNCTYPE(c_int, c_int)

def callback(value):
    print('callback called
