import ctypes
# Test ctypes.CFUNCTYPE on a simple function

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple integer-returning function
