import ctypes
# Test ctypes.CFUNCTYPE with a function that returns void.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# void func(int)
