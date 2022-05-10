import ctypes
# Test ctypes.CFUNCTYPE()

# ctypes.CFUNCTYPE()
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# Create a C callable function type.
#
# The restype and argtypes specify the result and argument types.
#
# If use_errno is True, the function will set the Python exception OSError
# if the C function returns -1, and the Python exception ValueError if the
# C function returns NULL.
#
# If use_last_error is True, the function will set the Python exception
# OSError if the C function returns 0.
#
# The OSError instance will have errno set to the value returned by a call
# to ctypes.get_errno().
#
# The ValueError instance will have its message set to the value returned
# by a call to ctypes.get_errno().
#
# The use_errno and use_last_error arguments are not supported on Windows.

import ctypes

# prototype
# int printf
