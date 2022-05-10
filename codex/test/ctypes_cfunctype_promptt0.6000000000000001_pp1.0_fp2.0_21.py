import ctypes
# Test ctypes.CFUNCTYPE(None) and ctypes.CFUNCTYPE(ctypes.c_int)
# without a prototype.

import _ctypes_test

dll = ctypes.CDLL(_ctypes_test.__file__)

