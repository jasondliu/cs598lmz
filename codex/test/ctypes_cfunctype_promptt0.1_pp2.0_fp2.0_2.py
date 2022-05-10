import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this function is declared as:
# void func(void (*callback)())

CALLBACK = ctypes.CFUNCTYPE(None)

