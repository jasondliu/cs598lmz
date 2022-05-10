import ctypes
# Test ctypes.CFUNCTYPE works okay.

import ctypes, sys

selfname = sys.argv[0]

libc = ctypes.CDLL(None)

atoi = libc.atoi

myatoi = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(atoi)

