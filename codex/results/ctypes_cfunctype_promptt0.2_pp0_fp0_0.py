import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    return x + 1

# This is the prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the actual function we want to call
func_ptr = prototype(func)

# This is the function we want to replace
def func2(x):
    return x + 2

# This is the prototype of the function we want to replace
prototype2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the actual function we want to replace
func2_ptr = prototype2(func2)

# This is the function we want to replace
def func3(x):
    return x + 3

# This is the prototype of the function we want to replace
prototype3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the actual function we want to replace
func3_ptr = prototype3(func
