import ctypes
# Test ctypes.CFUNCTYPE()
# This is used to create callback functions
# See also:
# http://docs.python.org/2/library/ctypes.html#ctypes.CFUNCTYPE

# Note: ctypes.CFUNCTYPE is used to create callback functions
# Note: ctypes.CFUNCTYPE is used to create callback functions
# Note: ctypes.CFUNCTYPE is used to create callback functions

# This is a function that will be called by the callback function
def py_func(a, b):
    print "py_func() called: a = %d, b = %d" % (a, b)
    return a + b

# This is a callback function
# The first parameter is the return type
# The rest of the parameters are the arguments
# Note: the rest of the parameters are passed as a tuple
# Note: the rest of the parameters are passed as a tuple
# Note: the rest of the parameters are passed as a tuple
cf_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c
