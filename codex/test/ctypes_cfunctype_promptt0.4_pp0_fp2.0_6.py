import ctypes
# Test ctypes.CFUNCTYPE()

# This is a test of ctypes.CFUNCTYPE.  It should print "2" and "3"

import ctypes

# Define a function pointer type

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Define a function that takes a function pointer as an argument

def func(f, arg):
    return f(arg)

# Create a function pointer from a Python callable

f = prototype(lambda x, y: x+y)

# Call the function with the function pointer

