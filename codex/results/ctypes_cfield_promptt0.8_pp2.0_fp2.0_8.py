import ctypes
# Test ctypes.CField
class Struct:
    _fields_ = [('a', ctypes.c_int)]

print type(Struct.a)
class Struct(ctypes.Structure):
    pass
Struct.b = ctypes.c_int
print type(Struct.b)
# Test ctypes.c_void_p.from_param()
from ctypes import *
from _ctypes import _CFuncPtr

class RestypeUnion:
    pass

RestypeUnion.from_param = c_void_p.from_param

try:
    RestypeUnion()
    print "Error!"
except TypeError:
    pass

from _ctypes import CFuncPtrType

class RestypeUnion:
    pass

RestypeUnion.from_param = CFuncPtrType.from_param

try:
    RestypeUnion()
    print "Error!"
except TypeError:
    pass

class A(object):
    pass

print CFuncPtrType.from_param(A) is None
# Test ctypes.Structure inheritance
class A(ctypes.Structure):

