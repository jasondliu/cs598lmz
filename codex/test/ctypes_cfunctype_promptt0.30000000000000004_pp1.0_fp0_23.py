import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer parameter

# The prototype is:
# int callit(int(*func)(int), int arg)

