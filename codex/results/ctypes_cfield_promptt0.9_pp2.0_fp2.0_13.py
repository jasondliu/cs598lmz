import ctypes
# Test ctypes.CField
#

import unittest
from test import test_support
from ctypes import _pointer_type_cache, _pointer_type

from sys import getrefcount as grc

class CFieldTestCase(unittest.TestCase):

    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]

    def test_cache(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        # "create" the pointer type
        type(X._fields_[0][1])

        # the pointer type should be cached now
        cache_size = len(_pointer_type_cache)
        self.assertTrue(X._fields_[0][1] in _pointer_type_cache)

        # the pointer types should be the same
        self.assertTrue(_pointer_type_cache[ctypes.c_int] is
                                       _pointer_type_cache[X._fields_[0][1]])

        # create a new Structure class
        class Y(
