import ctypes
# Test ctypes.CFUNCTYPE.
#
# The first argument of ctypes.CFUNCTYPE is the return type of the function,
# which is ctypes.c_int32 for the test functions below. The second argument
# is a tuple, the items of which are the argument types of the function.

# The first test function takes two arguments, both of type ctypes.c_int32.

# The second test function takes no arguments.

# The third test function takes one argument, which is a pointer to a
# function that takes no arguments and returns a ctypes.c_int32.

# The fourth test function takes one argument, which is a pointer to a
# function that takes no arguments and returns void.

# The fifth test function takes one argument, which is a pointer to a
# function that takes no arguments and returns void. However, the
# function pointer is passed as an argument to another function, so
# the type of the argument to test_function_5 is
# POINTER(CFUNCTYPE(None)), which is equivalent to
# CFUNCTYPE(None, restype=None).

# The sixth
