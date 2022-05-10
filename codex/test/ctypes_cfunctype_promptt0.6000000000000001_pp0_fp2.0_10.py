import ctypes
# Test ctypes.CFUNCTYPE()
#
# "PF" is a function pointer type.
#
# XXX: we need to call the ctypes function, because otherwise
# ctypes doesn't detect the function pointer type.
# (This is a known bug in ctypes, reported in SF bug #1888667).

import _ctypes_test

def func(a,b):
    return 1

# XXX: we need to call the ctypes function, because otherwise
# ctypes doesn't detect the function pointer type.
# (This is a known bug in ctypes, reported in SF bug #1888667).

