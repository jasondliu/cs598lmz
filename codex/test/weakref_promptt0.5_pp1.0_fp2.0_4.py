import weakref
# Test weakref.ref()
import operator
import gc
import unittest

class TestWeakref(unittest.TestCase):
    def test_basic(self):
        x = TestWeakref.C()
        y = weakref.ref(x)
        self.assertEqual(y(), x)
        x2 = y()
        self.assertEqual(x2, x)
        self.assertEqual(x2.__class__, TestWeakref.C)
        x3 = y()
        self.assertEqual(x3, x)
        del x, x2, x3
        self.assertEqual(gc.collect(), 1)
        self.assertEqual(y(), None)
        self.assertEqual(gc.collect(), 0)

    def test_callable(self):
        x = TestWeakref.C()
        y = weakref.ref(x)
        self.assertEqual(y(), x)
        self.assertEqual(y(), x)
        self.assertEqual(y(), x)
        del x
