import ctypes
# Test ctypes.CFUNCTYPE
#
# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# restype: the result type
# argtypes: tuple of argument types
# use_errno: if TRUE, the function will set the external variable errno
#            to the last error code if the function failed.
# use_last_error: if TRUE, the function will set the external variable
#                 GetLastError() to the last error code if the function
#                 failed.
#
# CFUNCTYPE creates a callback function prototype.
#
# The returned object is a callable object which can be passed
# as the first parameter to any of the functions in the ctypes.windll
# or ctypes.oledll module.
#
# The prototype of the callback function is determined by the
# restype and argtypes arguments.
#
# All functions in the Windows API that pass callback functions
# use stdcall calling convention.
#
# The callback function is called with the calling convention specified
# by the restype and argtypes arguments.
#
# If
