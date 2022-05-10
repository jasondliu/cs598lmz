import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

# A simple function
def func(a, b):
    return a + b

# Create a C callable function from the Python function
cfunc = CFUNCTYPE(c_int, c_int, c_int)(func)

# Call the C function
print(cfunc(1, 2))

# Create a C callable function from the Python function
cfunc = CFUNCTYPE(c_int, c_int, c_int)(func)

# Call the C function
print(cfunc(1, 2))

# Create a C callable function from the Python function
cfunc = CFUNCTYPE(c_int, c_int, c_int)(func)

# Call the C function
print(cfunc(1, 2))

# Create a C callable function from the Python function
cfunc = CFUNCTYPE(c_int, c_int, c_int)(func)

# Call the C function
print(cfunc(1, 2))

# Create a C callable
