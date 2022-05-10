import ctypes
# Test ctypes.CFUNCTYPE()
#

import sys
import ctypes
from ctypes import *

def test(typ):
    f = CFUNCTYPE(typ)
    print f()

for typ in [c_int, c_long, c_double, c_char_p, POINTER(c_int)]:
    print typ
    test(typ)

if sizeof(c_long) == sizeof(c_void_p):
    test(c_void_p)

if sizeof(c_longlong) == sizeof(c_void_p):
    test(c_longlong)

if sizeof(c_longdouble) == sizeof(c_void_p):
    test(c_longdouble)

if sizeof(c_ulong) == sizeof(c_void_p):
    test(c_ulong)

if sizeof(c_ulonglong) == sizeof(c_void_p):
    test(c_ulonglong)
