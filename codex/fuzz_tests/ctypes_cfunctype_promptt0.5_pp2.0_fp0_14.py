import ctypes
# Test ctypes.CFUNCTYPE
#
# We test the following functions:
#
# - ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
#   Create a wrapper for C callback functions.
#
# - ctypes.WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
#   Create a wrapper for Windows callback functions.
#
# - ctypes.PYFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
#   Create a wrapper for Python callback functions.
#
# - ctypes.CFUNCTYPE.errcheck(func)
#
#   Add an error check function to the callback type.
#
# - ctypes.CFUNCTYPE.restype(restype)
#
#   Set the result type for the callback type.
#
# - ctypes.CFUNCTYPE.argtypes(argtypes)
#
#   Set the argument types
