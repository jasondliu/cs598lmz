import ctypes
# Test ctypes.CFieldType.from_param.
from ctypes import *
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X), ("b", c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y), ("c", c_int)]

class MyInt(c_int):
    def _CData_output(self, resbuf, base=None, name=None, internal=False, typecode=None):
        return ctypes.c_int(self)._CData_output(resbuf, base, name, internal, typecode)

class MyUInt(c_uint):
    def _CData_output(self, resbuf, base=None, name=None, internal=False, typecode=None):
        return ctypes.c_uint(self)._CData_output(resbuf, base, name, internal, typecode)

class MyWChar(c_
