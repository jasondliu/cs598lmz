import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is used to determine whether the compiler is capable of
# generating the correct function type for CFUNCTYPE.  This is used to
# determine whether the tests for calling functions with the 'f' code
# should be skipped.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

