import ctypes
# Test ctypes.CFUNCTYPE()
#
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# Create and return a new function prototype.
#
# restype is the result type, argtypes is a tuple of argument types.
#
# The function prototype is used to create C callable function from Python
# callable objects.
#
# If use_errno is True, the function will set the global variable
# 'ctypes.errno' to the error code returned by the function.  If
# use_last_error is True, the function will call 'ctypes.GetLastError()'
# after the call, and store the result in the 'ctypes.LastError'
# variable.
#
# Example:
#
#  from ctypes import *
#  cdll.msvcrt.malloc.restype = c_void_p
#  cdll.msvcrt.malloc.argtypes = (c_int,)
#
#  def my_malloc(size):
#      return cdll
