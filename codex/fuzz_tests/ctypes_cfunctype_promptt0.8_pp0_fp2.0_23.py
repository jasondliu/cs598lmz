import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

lib = ctypes.CDLL(ctypes.util.find_library("m"))

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
c_log = prototype(("log", lib))

print c_log(2)
