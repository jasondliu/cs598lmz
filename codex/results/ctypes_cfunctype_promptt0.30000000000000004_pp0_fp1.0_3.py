import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type, default is c_int
# argtypes: the argument types, default is None
# use_errno: if True, the function will set the global variable errno
# use_last_error: if True, the function will set the global variable
#                 GetLastError()

# The function prototype is:
# int function(int a, int b)
#
# The function returns the sum of the two arguments.

# The function prototype is:
# int function(int a, int b)
#
# The function returns the sum of the two arguments.

# The function prototype is:
# int function(int a, int b)
#
# The function returns the sum of the two arguments.

# The function prototype is:
# int function(int a, int b)
#
# The function
