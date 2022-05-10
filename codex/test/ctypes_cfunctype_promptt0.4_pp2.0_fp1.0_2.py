import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#

# This is the prototype of the function we will call:
# int double(int)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Now we get the address of the 'double' function in the _ctypes_test
# shared lib, and assign it to a Python variable.

