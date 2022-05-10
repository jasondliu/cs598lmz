import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will set the global variable errno
#            if a non-zero value is returned
# use_last_error: if True, the function will set the Win32 last error
#                 value if a non-zero value is returned

# XXX Should we use a callback function here?

# XXX We should test the use_errno and use_last_error flags

# XXX We should test the alignment of the arguments on the stack

# XXX We should test the alignment of the result on the stack

# XXX We should test the alignment of the arguments in memory

# XXX We should test the alignment of the result in memory

# XXX We should test the alignment of the arguments in registers

# XXX We should test the alignment of
