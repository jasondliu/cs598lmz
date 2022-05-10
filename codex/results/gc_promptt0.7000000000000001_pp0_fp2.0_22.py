import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Test all_objects()

from weakref import proxy, getweakrefcount
from gc import get_objects, get_referrers
import unittest
from test import test_support
import sys

class GCTests(unittest.TestCase):
    def test_getweakrefcount(self):
        # Verify getweakrefcount() returns 0 for non-weakrefable objects
        class NonWeakRefable:
            pass
        a = NonWeakRefable()
        self.assertEqual(getweakrefcount(a), 0, "expected 0 weak refs")

    if hasattr(sys, 'gettotalrefcount'):
        def test_gettotalrefcount(self):
            # Verify gettotalrefcount() returns 0 for objects without
            # cyclic gc
            a = []
            self.assertEqual(sys.gettotalrefcount(a), 0, "expected 0 refs")

    def test_getreferents(self):
        # Verify getreferents()
        a = []
        self.assertEqual(gc.get_ref
