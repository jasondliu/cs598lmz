import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the case where the function is called with a
# result type that is not compatible with the declared result type.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function returns a pointer to an integer.  But we call it
# with a pointer to a character.  This should result in a
# TypeError exception.

