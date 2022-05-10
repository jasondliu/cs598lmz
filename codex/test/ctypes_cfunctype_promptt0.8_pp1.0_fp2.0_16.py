import ctypes
# Test ctypes.CFUNCTYPE
prototype = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int, ctypes.c_int )
paramflags = ( 1, "a", 0 ), ( 1, "b", 0 )

import _ctypes_test
