import ctypes
# Test ctypes.CFUNCTYPE

# Test calling a function pointer
#
# NOTE: this test is NOT run by default.  To run it,
# edit the Makefile and change the line:
#
# TEST_CFLAGS = -DTEST_RUN_CTYPES_CFUNCTYPE
#
# to:
#
# TEST_CFLAGS = -DTEST_RUN_CTYPES_CFUNCTYPE=1
#
# and then run 'make test'.

import _ctypes_test

libc = ctypes.CDLL(_ctypes_test.__file__)

