import weakref
# Test weakref.ref
import sre
import _sre
import test.test_support
import unittest
import sys
# Use weak references to hold our test objects.
class TestObject(object):
    pass
class BasicTest(unittest.TestCase):
    def test_ref(self):
        expected = TestObject()
        p = weakref.ref(expected)
        self.assertEqual(p(), expected)
        self.assertEqual(p.__call__(), expected)
        self.assertEqual(p.__hash__(), hash(expected))
        self.assertEqual(p.__eq__(expected), True)
        self.assertEqual(p.__ne__(expected), False)
        self.assertEqual(p.__eq__(object()), False)
        self.assertEqual(p.__ne__(object()), True)
        self.assertEqual(p.__eq__(p), True)
        self.assertEqual(p.__ne__(p), False)
        self.assertEqual(p.__eq__(p
