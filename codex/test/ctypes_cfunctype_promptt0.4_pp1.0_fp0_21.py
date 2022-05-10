import ctypes
# Test ctypes.CFUNCTYPE
# https://docs.python.org/2/library/ctypes.html#ctypes.CFUNCTYPE

import ctypes

# C prototype of the callback function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

