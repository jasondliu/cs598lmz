import ctypes
# Test ctypes.CFUNCTYPE
# CFUNCTYPE is the simplest way to create a callback.
# You can use CFUNCTYPE to create type objects for callback functions.
# The first argument is a list of the argument types,
# the second argument is the return type.
# The following code creates a callback function that takes a number
# and returns the square of that number:

# Define a function taking one integer argument and returning an integer.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# Convert the Python number to a c_int and pass it to the C function.
# Return a Python integer from the result.
def py_cmp_func(a, b):
    print("py_cmp_func a:", a, "b:", b)
    return a - b
# Callback functions must be able to accept None as an argument.
# If they can't, then an exception will be raised.
# This is because the function may be called with None as the first argument.
# The None is the finalizer callback, and it should be called when

