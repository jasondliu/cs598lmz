import weakref
# Test weakref.refcycle()
import _weakref

import unittest
from test import test_support

# Mock object class
class C:
    pass

class BaseWeakrefTestCase(unittest.TestCase):
    # Base class for weakref tests.

    # Subclasses must define self.thetype.

    # Some tests define their own thetype.
    # Some tests use weakref.ref for self.thetype.

    def setUp(self):
        self.thing = self.thetype(C())

    def test_simple(self):
        # Create a weak reference
        p = self.thing
        self.assertEqual(p(), C())
        self.assertEqual(type(p), self.thetype)
        self.assertEqual(p is self.thing, True)
        self.assertEqual(p == self.thing, True)
        self.assertEqual(p != 23, True)
        self.assertEqual(self.thing, p)
        self.assertEqual(23, self.thing)
        self.assertEqual(23 !=
