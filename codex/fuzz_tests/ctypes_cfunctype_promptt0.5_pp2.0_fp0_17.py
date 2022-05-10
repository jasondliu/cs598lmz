import ctypes
# Test ctypes.CFUNCTYPE
#
# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# Create a C callable function from a Python callable.
#
# restype: the result type, or None if the function returns None
# argtypes: a list of the argument types
# use_errno: if True, the calling convention will check for errors and raise
#            an OSError if the function returned -1
# use_last_error: if True, the calling convention will check for errors and
#                 raise an OSError if the function returned NULL
#
# The returned function checks the return value for errors as specified by
# use_errno and use_last_error.
#
# If the function returned -1, it will raise an OSError exception with the
# corresponding errno value.
#
# If the function returned NULL, it will raise an OSError exception with the
# corresponding GetLastError() value.
#
# If the function returned a string, the returned string is converted to a
# Python string using the
