import ctypes
# Test ctypes.CFUNCTYPE works okay.

import ctypes, sys

selfname = sys.argv[0]

libc = ctypes.CDLL(None)

atoi = libc.atoi

myatoi = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(atoi)

if myatoi("42") != 42:
    print "%s: CFUNCTYPE(function) did not work" % (selfname)
    sys.exit(1)
