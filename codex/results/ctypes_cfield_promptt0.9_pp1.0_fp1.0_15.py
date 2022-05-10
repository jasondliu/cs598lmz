import ctypes
# Test ctypes.CField.

import ctypes.test.test_cfield as test_cfield
import unittest
#import ctypes

class X(ctypes.Structure):
    _fields_ = [('xx', ctypes.c_int)]

class Y(ctypes.Structure):
    pass
Y._fields_ = [('y', X)]

class TypeARRAYTestCase(test_cfield.TypeARRAYTestCase):
    y = Y()
    y.y.xx = 42
    def check_pointer(self, name):
        try:
            self.failUnlessEqual(getattr(self.y, name)[0].contents, 42)
        except AttributeError:
        # handle bug in ctypes
            raise AttributeError("TypeARRAYTestCase.check_pointer")

    def check_byref(self, name):
        try:
            self.failUnlessEqual(getattr(self.y, name)[0], 42)
        except AttributeError:
            # handle bug in ctypes
            raise AttributeError("TypeARRAYTestCase.check
