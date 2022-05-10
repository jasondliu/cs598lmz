import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX This is a hack.  We should really be using a real C compiler
# to compile a shared library.
#
# The following is a C function that takes a function pointer as
# argument.  The function pointer is called with an integer argument,
# and the C function returns the result of the call.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callbackfunc(arg):
    print("callbackfunc", arg)
    return arg * 2

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def cmpfunc(a, b):
    print("cmpfunc", a, b)
    return a - b

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure
