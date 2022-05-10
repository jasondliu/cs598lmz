import ctypes
# Test ctypes.CFUNCTYPE for callbacks

from ctypes import *

from ctypes.test import is_resource_enabled

try:
    set
except NameError:
    from sets import Set as set

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(Structure):
    _fields_ = [("b", c_int)]

class Z(Union):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class XX(Structure):
    _fields_ = [("x", X),
                ("y", Y)]

class YY(Structure):
    _fields_ = [("x", Y),
                ("y", X)]

class ZZ(Structure):
    _fields_ = [("x", Z),
                ("y", Z)]

class A(Structure):
    _fields_ = [("a", c_int)]

class B(Structure):
    _fields_ = [("a", c_int)]

class C(Structure):
    _
