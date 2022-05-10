import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is not exported by the dll, so using
# a function pointer is the only way to call it.
#
# Hm, cdecl calling convention is the default on Windows...
