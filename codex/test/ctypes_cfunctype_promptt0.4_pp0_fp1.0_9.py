import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

def func(x):
    return x + 1

# Create a C function pointer prototype
CMPFUNC = CFUNCTYPE(c_int, c_int)

# Convert the Python function to a C function pointer
cfunc = CMPFUNC(func)

# Call the C function pointer
print(cfunc(1))

# Create a C function pointer prototype
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

# Convert the Python function to a C function pointer
cfunc = CMPFUNC(func)

# Call the C function pointer
print(cfunc(1, 2))

# Create a C function pointer prototype
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, c_int)

# Convert the Python function to a C function pointer
cfunc = CMPFUNC(func)

# Call the C function pointer
print(cfunc(1, 2, 3))

# Create a C function pointer prototype
CMPFUNC
