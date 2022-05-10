import ctypes
# Test ctypes.CFUNCTYPE
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

# restype
# The result type. This must be a ctypes type.

# argtypes
# A sequence specifying the argument types. Each item in the sequence must be a ctypes type.

# use_errno
# If True, the function will set the ctypes.get_errno() to the value returned by the function.

# use_last_error
# If True, the function will set the ctypes.get_last_error() to the value returned by the function.

# The function prototype is given by restype and argtypes. The function prototype is the same as the one used by the WINFUNCTYPE and WINAPI macros in the Windows API.

# The function returns a callable object which when called invokes the function.

# The callable object also has a restype and argtypes attribute which are read-only.

# The callable object also has a _flags_ attribute which is a bitmask of the flags used by the function. The
