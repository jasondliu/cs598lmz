import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# This is the prototype of the callback function
# It must be a cdecl function, taking an integer argument,
# and returning an integer.

PROTO = CFUNCTYPE(c_int, c_int)

def addressof(cfunc):
    return c_void_p.from_address(addressof(cfunc._ptr._obj))

def callback(arg):
    print "callback called with", arg
    return arg

# This is the prototype of the function taking the callback
# It must be a cdecl function, taking a CFUNCTYPE instance as first
# argument, and an integer as second argument.

CALLBACKFUNC = CFUNCTYPE(c_int, PROTO, c_int)

# This is the function taking the callback.  It is implemented in C.

_callbackfunc = dll.callbackfunc
_callbackfunc.argtypes = (CALLBACKFUNC, c_int)
_callbackfunc.restype = c_int

def callbackfunc(func, arg):
    return _
