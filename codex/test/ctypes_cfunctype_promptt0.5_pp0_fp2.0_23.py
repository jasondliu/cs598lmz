import ctypes
# Test ctypes.CFUNCTYPE()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: a bool indicating whether the function uses the C errno variable
# use_last_error: a bool indicating whether the function uses the Win32 GetLastError() function

# ctypes.CFUNCTYPE() is used to create C callable function pointers from Python callables.
# The returned function pointer can be called in the usual way, i.e. function(arg1, arg2, ...)

# The arguments are the same as for ctypes.WINFUNCTYPE() and ctypes.CFUNCTYPE()

# The result type must be a ctypes type, and the argument types must be ctypes types as well.

# The use_errno and use_last_error flags are not used on non-Windows platforms.

# The function pointer can be passed to other C functions expecting a function pointer with the same signature.

# The function
