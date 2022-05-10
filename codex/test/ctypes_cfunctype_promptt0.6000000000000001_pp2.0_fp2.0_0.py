import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

