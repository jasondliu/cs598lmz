import ctypes
# Test ctypes.CFUNCTYPE by using a function that returns a pointer to a function.

import ctypes

libc = ctypes.CDLL(None)

f = libc.getenv
f.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

g = f("PATH")
assert g("PATH") == 0
assert g("PATH2") != 0

print 'OK'
