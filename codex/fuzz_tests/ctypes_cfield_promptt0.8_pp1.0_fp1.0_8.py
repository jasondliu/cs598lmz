import ctypes
# Test ctypes.CField.from_param()
from ctypes import *
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

##############

## POINTER(POINTER(c_int))

c_int_p_p = POINTER(POINTER(c_int))

def ptr_ptr_of_ints(n):
    return (c_int * n)()

lib.ptr_ptr_of_ints.restype = c_int_p_p

ppi = lib.ptr_ptr_of_ints(5)
ppi[0][0] = 42
assert ppi[0][0] == 42

class X(Structure):
    _fields_ = [("p", c_int_p_p)]

lib.ptr_ptr_of_ints.restype = c_int_p_p

x = X()
x.p = lib.ptr_ptr_of_ints(5)
x.p[0][0] = 42
assert x.p[0][0] == 42

class Y(Union
