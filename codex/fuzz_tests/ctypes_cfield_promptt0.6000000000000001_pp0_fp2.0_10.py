import ctypes
# Test ctypes.CField instances
import gc
import unittest
from test import test_support

class TestField(unittest.TestCase):
    def test_none(self):
        # None as typecode is allowed, since ctypes allows None as _type_
        # attribute.
        self.assertEqual(ctypes._CField(None, None, None, None).offset, 0)

    def test_gc(self):
        # Issue #18874: ctypes._CField instances are not tracked by the GC.
        class X(ctypes.Structure):
            _fields_ = [('x', ctypes.c_long)]
        self.assertEqual(len(gc.get_referrers(X.x)), 2)


class TestStructure(unittest.TestCase):
    def test_create_instance(self):
        class X(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int)]
        self.assertEqual(X._fields_, [('x', ctypes.c_int)])
        self.assertEqual
