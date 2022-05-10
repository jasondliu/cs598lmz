import ctypes
# Test ctypes.CFUNCTYPE

# This is a simple test of the CFUNCTYPE() function.

from ctypes import *

# First, define a function pointer type.
# This is a function that takes an int and returns an int.
# The first argument is the return type, the rest are the argument types.

prototype = CFUNCTYPE(c_int, c_int)

# Now, create a function that takes an int and returns an int.

def py_func(i):
    return i + 1

# Now, create a C function from the Python function.

c_func = prototype(py_func)

# Now, call the C function.

assert c_func(2) == 3

# Now, create a C function that takes a function pointer.

def call_func(func, arg):
    return func(arg)

call_func_c = CFUNCTYPE(c_int, c_int)(call_func)

# Now, call the C function.

assert call_func_c(c_func, 2) == 3

# Now
