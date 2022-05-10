import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is called with an integer argument, and returns the
# square of this number. 

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Callback functions must be registered using a Python
# function, with a C prototype.

# This function takes a function pointer as argument, and calls
# the function with an integer argument.

lib.callit.restype = ctypes.c_int
lib.callit.argtypes = (CMPFUNC,)

def my_callback(n):
    print "my_callback was called with", n
    return n * n

# The following line is equivalent to
#   result = lib.callit(my_callback)
# except that the function is wrapped in a CFUNCTYPE object.

result = lib.callit(CMPFUNC(my_callback))
print "result", result
