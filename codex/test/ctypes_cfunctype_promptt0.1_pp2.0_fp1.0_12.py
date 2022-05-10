import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a pointer argument
#
# prototype:
#   int func(int *p)
#
# call:
#   func(&i)

