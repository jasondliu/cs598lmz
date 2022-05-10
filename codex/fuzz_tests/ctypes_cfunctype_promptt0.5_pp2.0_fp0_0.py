import ctypes
# Test ctypes.CFUNCTYPE
#
# A function type that can be used as a callback.
#
# This is similar to the ctypes.CFUNCTYPE class, except that this
# class allows you to specify the calling convention of the function.
#
# The calling convention is specified as one of the following constants:
# - ctypes.WINFUNCTYPE for WINAPI functions.
# - ctypes.CFUNCTYPE for C functions.
# - ctypes.PYFUNCTYPE for Python functions.
# - ctypes.DUMMYFUNCTYPE for functions that do nothing.
#
# The default calling convention is WINAPI.

# ctypes.WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# ctypes.PYFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# ctypes.DUMMYFUN
