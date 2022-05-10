import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The rest of the file is a modified copy of _ctypes_test.c
#

#
# Test CFUNCTYPE(c_int, c_int)
#

