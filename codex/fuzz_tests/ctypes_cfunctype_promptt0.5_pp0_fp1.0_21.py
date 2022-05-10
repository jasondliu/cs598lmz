import ctypes
# Test ctypes.CFUNCTYPE
#
# Types are specified by name, or as a ctypes instance.
#
# The function will be called with arguments according to
# the types given, and the result type.
#
# The function will be called with a pointer to the arguments
# as the first parameter.  The second parameter is a pointer
# to a result.  The result is a pointer to the result value.
#
# The function must return 0 on success, and -1 if the
# arguments are invalid.
#
# The function may be called with None as the first parameter
# to check the argument types.  In this case, the function
# must return the number of arguments.
#
# The function may be called with None as the second parameter
# to check the result type.  In this case, the function must
# return the number of results.
#
# The function may be called with None as the first and second
# parameter.  In this case, the function must return the number
# of arguments, followed by the number of results.
#
# The function may be called with a tuple as the first parameter,
# in which case the arguments
