import ctypes
# Test ctypes.CField

import ctypes
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Y(Structure):
    _fields_ = [("x", X),
                ("y", c_int)]

class Z(Structure):
    _fields_ = [("x", X),
                ("y", c_int),
                ("z", c_int)]

class XX(Structure):
    _fields_ = [("a", X),
                ("b", c_int)]

# simple

from ctypes import _CData, _CDataMeta
from ctypes import _Pointer
from ctypes import CField, CFieldMeta

class C(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

field_a = CField("a", C, c_int)
assert isinstance(field_a, CField)
assert field
