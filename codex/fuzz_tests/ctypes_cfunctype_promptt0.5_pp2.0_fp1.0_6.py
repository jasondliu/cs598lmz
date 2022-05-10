import ctypes
# Test ctypes.CFUNCTYPE()

import _ctypes_test

try:
    from _ctypes import FreeLibrary
except ImportError:
    from ctypes import FreeLibrary

libc = ctypes.CDLL(ctypes.util.find_library("c"))

def callback(arg):
    print("callback", arg)
    return arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# install the callback
buf = (ctypes.c_int * 1)(0)
libc.qsort(buf, 1, ctypes.sizeof(ctypes.c_int), CMPFUNC(callback))

# this should fail because the callback is still installed
try:
    libc.qsort(buf, 1, ctypes.sizeof(ctypes.c_int), None)
except TypeError:
    print("TypeError")

# uninstall the callback
CMPFUNC(None)

# this should work now
libc.qsort(buf, 1, ctypes.sizeof(ctypes.c_
