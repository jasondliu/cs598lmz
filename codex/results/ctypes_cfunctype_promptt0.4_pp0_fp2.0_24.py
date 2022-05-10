import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

# prototype of the C function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# create a C function
def my_function(x):
    return x + 1

# convert the Python function into a C function
cfunc = prototype(my_function)

# call the C function
result = cfunc(1)

print(result)

# Test ctypes.POINTER()

import ctypes

# prototype of the C function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# create a C function
def my_function(x):
    return x[0] + 1

# convert the Python function into a C function
cfunc = prototype(my_function)

# call the C function
result = cfunc(ctypes.byref(ctypes.c_int(1)))

print(result)

# Test ctypes.c_float()

import ctypes


