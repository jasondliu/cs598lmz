import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX On Win64, the calling convention is ignored, and cdecl is always used.
# This is a bug in ctypes.

# cdecl
