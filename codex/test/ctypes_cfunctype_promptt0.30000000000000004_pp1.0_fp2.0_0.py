import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# use_errno and use_last_error are Windows specific.

# XXX This is not tested yet:
#
# Calling a function with a prototype that has use_errno or use_last_error
# set, and the function returns -1, sets the error indicator and returns
# None.

# XXX This is not tested yet:
#
# If the function returns a pointer, and the pointer is NULL, the error
# indicator is set and None is returned.

# XXX This is not tested yet:
#
# If the function returns a pointer, and the pointer is not NULL, but the
# contents of the memory the pointer points to is NULL, the error indicator
# is set and None is returned.

# XXX This is not tested yet:
#
# If the function returns a pointer, and the pointer is not NULL, and the

