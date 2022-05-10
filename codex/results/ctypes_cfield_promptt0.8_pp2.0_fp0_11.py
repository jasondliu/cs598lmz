import ctypes
# Test ctypes.CField.from_address()
from ctypes import *

import _ctypes_test

if _ctypes_test.MyCFuncPtr is None:
    raise Exception("_ctypes_test.MyCFuncPtr is NULL")

if type(_ctypes_test.MyCFuncPtr) is not CFUNCTYPE:
    raise Exception("_ctypes_test.MyCFuncPtr is not a CFUNCTYPE object")

MyCFuncPtr = CFUNCTYPE(c_int)(_ctypes_test.MyCFuncPtr)

##############################

class X(Structure):
    _fields_ = [("val", c_int)]

class Y(Structure):
    _fields_ = [("x", POINTER(X))]


x = ctypes.c_int(23)
y = Y.from_address(ctypes.addressof(x))

if y.x.contents.value != 23:
    raise Exception("Value should be 23: %d" % y.x.contents.value)

################################################################
#

