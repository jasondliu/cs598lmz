import ctypes
# Test ctypes.CFUNCTYPE()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# restype: The result type.
# argtypes: The argument types.
# use_errno: If True, the function will set the global variable errno
#            to the last error code after the call.
# use_last_error: If True, the function will set the global variable
#                 GetLastError() to the last error code after the call.

# The function will be called by using the function call operator.

# The function object created by CFUNCTYPE() takes one argument for each
# parameter expected by the C function, in the order they are declared.
# The function object created by CFUNCTYPE() contains the following read-only
# attributes:
#
# argtypes: Tuple of C data types for the arguments accepted by this function.
# restype: The C data type returned by this function.
# errcheck: If not None, the function will be called after the C function has
#           returned. The errcheck
