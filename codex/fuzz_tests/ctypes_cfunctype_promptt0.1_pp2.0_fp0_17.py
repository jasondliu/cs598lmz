import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will set the global variable errno
#            if an error occurs.
# use_last_error: if True, the function will set the Win32 last error
#                 value if an error occurs.

# XXX This is not yet implemented
# XXX use_errno and use_last_error are not yet implemented

# XXX This is not yet implemented
# XXX use_errno and use_last_error are not yet implemented

# XXX This is not yet implemented
# XXX use_errno and use_last_error are not yet implemented

# XXX This is not yet implemented
# XXX use_errno and use_last_error are not yet implemented

# XXX This is not yet implemented
# XXX use_err
