import ctypes
# Test ctypes.CFUNCTYPE

# This test is intended to be run with a debug build of Python.
# It will crash if the debug build is not used.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is not called, but it must be declared,
# otherwise the test will crash.
