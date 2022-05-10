import ctypes
# Test ctypes.CFUNCTYPE function
#
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#   restype: A C type, or a Python callable returning a C type, which is used
#            to convert the return value from the function.
#   argtypes: A list of C types.
#   use_errno: If True, the function will set the global C variable errno
#              upon error.
#   use_last_error: If True, the function will set the Windows last error
#                   upon error.
#
# Note:
#   ctypes.CFUNCTYPE is used to create a function prototype. It returns a
#   callable object that can be used to create callbacks.
#   The function prototype is saved in ctypes._CFuncPtr object.
#
#   ctypes.CFUNCTYPE(restype, *argtypes, **kwds) -> <class '_ctypes.CFuncPtr'>
#
#   The callable object is saved in ctypes._CFuncPtr_func_type
