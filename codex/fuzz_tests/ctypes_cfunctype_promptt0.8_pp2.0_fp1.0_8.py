import ctypes
# Test ctypes.CFUNCTYPE.
# If this fails, you probably have a broken gcc install.
if ctypes.CFUNCTYPE(ctypes.c_int) == ctypes.CFUNCTYPE(ctypes.c_int):
    cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char)(lambda: 0)

# from __future__ import print_function
import sys
# try:
#     print('hi', file=sys.stderr)
# except Exception as e:
#     print('Print is your friend.')
#     print(e)
#     sys.exit(-1)


def check_sizeof(typ, expected):
    actual = ctypes.sizeof(typ)
    if actual != expected:
        s = 'expected %s to have sizeof %d, but it has %d'
        raise RuntimeError(s % (typ, expected, actual))


# sanity check ctypes
check_sizeof(ctypes.c_void_p, _sizeof_p)
del check_sizeof

from ctypes import CD
