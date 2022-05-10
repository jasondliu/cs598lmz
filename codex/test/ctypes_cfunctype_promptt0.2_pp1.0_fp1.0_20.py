import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# This is the prototype of the callback function
# It must be a cdecl function, taking an integer argument,
# and returning an integer.

PROTO = CFUNCTYPE(c_int, c_int)

def addressof(cfunc):
    return c_void_p.from_address(addressof(cfunc._ptr._obj))

