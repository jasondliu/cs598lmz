import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False)
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=True)

# void func(int)
