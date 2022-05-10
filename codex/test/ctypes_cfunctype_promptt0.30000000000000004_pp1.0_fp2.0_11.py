import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# test CFUNCTYPE(None)

# This function raises an exception, so we must call it with
# CFUNCTYPE(None)(), so the exception is not printed.
