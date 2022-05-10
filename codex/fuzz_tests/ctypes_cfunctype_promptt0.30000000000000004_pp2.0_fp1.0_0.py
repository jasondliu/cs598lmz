import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: the argument types
# use_errno: if True, the function will set the global variable errno
#            if an error occurs.
# use_last_error: if True, the function will set the Win32 last error
#                 code if an error occurs.

# The function must return an integer, which will be interpreted as
# a boolean value. If the integer is zero, the function call will
# raise an exception.

# The function must not raise an exception itself.

# The function must not return a value of type ctypes.c_char_p or
# ctypes.c_wchar_p.

# The function must not return a value of type ctypes.c_void_p.

# The function must not return a value of type ctypes.c_ulong
