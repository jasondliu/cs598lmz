import ctypes
# Test ctypes.CField and ctypes._Pointer.from_param
#
# To test from_param() we use it to get a function argument indexed
# by a CField.
#
import unittest
from ctypes import *
from ctypes.test import is_resource_enabled

class CFoo(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

class CTest(Structure):
    pass

class CTestPtr(POINTER(CTest)):
    pass

class CTest2(Structure):
    pass

class CTest2Ptr(POINTER(CTest2)):
    pass

class CTest3(Union):
    pass

class CTest3Ptr(POINTER(CTest3)):
    pass

class CFooPtr(POINTER(CFoo)):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, CFoo):
            return cls(value)
        return value

## default from_param():
##
##    @classmethod

