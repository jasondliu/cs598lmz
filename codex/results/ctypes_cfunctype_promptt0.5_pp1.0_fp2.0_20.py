import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.POINTER(), and ctypes.cast()
from ctypes import *
from ctypes.test import need_symbol

################################################################
#
# Some helper functions

def check_type(obj, typ):
    if type(obj) is not typ:
        raise TypeError("%s is not %s" % (obj, typ))

def check_value(obj, val):
    if obj != val:
        raise ValueError("%s is not %s" % (obj, val))

def check_address(obj, addr):
    if addressof(obj) != addr:
        raise ValueError("%s is not at %s" % (obj, hex(addr)))

################################################################
#
# Test ctypes.CFUNCTYPE()

# CFUNCTYPE() creates a C function pointer from a Python callable:

c_func = CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)
check_type(c_func, CFUNCTYPE(c_int, c
