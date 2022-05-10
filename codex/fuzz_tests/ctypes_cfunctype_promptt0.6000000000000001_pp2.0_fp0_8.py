import ctypes
# Test ctypes.CFUNCTYPE
#
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False) -> function prototype
#
# Create a C callable function prototype object.
#
# restype is the result type. argtypes is a tuple of argument types.
# The function prototype can be called with any number of arguments,
# as long as they are compatible with the types given in argtypes.
#
# If use_errno is True, the function will set the exception errno on error.
# If use_last_error is True, the function will set the exception ctypes.GetLastError() on error.
#
# The returned function prototype is callable, and accepts the following keyword arguments:
# - calling_convention: The calling convention, that is ctypes.WINFUNCTYPE or ctypes.CFUNCTYPE.
# - error_check: If True, raise an exception on error. If a callable is specified, it will be called with an integer parameter specifying the error code.
# - use_errno: If True, the function will set the exception
