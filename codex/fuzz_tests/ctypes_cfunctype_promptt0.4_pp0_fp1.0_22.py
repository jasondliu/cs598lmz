import ctypes
# Test ctypes.CFUNCTYPE()
#
# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# Creates a C callable function prototype instance, which can be used to create
# C callable functions from Python callables.
#
# The returned prototype instance is callable itself, and when called it
# creates a callable object that when called invokes the underlying C function.
#
# The prototype can also be called with a C function address as its first
# argument. In this case, it creates a callable object that calls the C
# function directly.
#
# The restype and argtypes specify the result and argument types of the C
# function. They can be types from ctypes, or anything that can be converted
# to a ctypes type, like types from the standard Python library.
#
# The optional use_errno and use_last_error keyword arguments specify whether
# the C function should set the C errno variable or the Win32 last error code
# when it returns an error indication.
#
# The optional keyword argument kwds can be used to
