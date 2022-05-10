import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# define a function
def myfunc(a, b):
    return a + b

# cast the function to the prototype
myfunc_c = prototype(myfunc)

# call the function
print(myfunc_c(1, 2))

# Test ctypes.POINTER()

import ctypes

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# define a function
def myfunc(a):
    return a[0]

# cast the function to the prototype
myfunc_c = prototype(myfunc)

# call the function
a = (ctypes.c_int * 1)(1)
print(myfunc_c(a))

# Test ctypes.byref()

import ctypes

# prototype a function
