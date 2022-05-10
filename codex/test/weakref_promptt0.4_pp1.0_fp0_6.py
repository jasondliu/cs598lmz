import weakref
# Test weakref.ref
import gc
import unittest

class Foo:
    pass

class WeakRefTestCase(unittest.TestCase):

    def test_basic(self):
        f = Foo()
        r = weakref.ref(f)
        self.assertEqual(r(), f)
        self.assertEqual(r.__call__(), f)
        self.assertEqual(r.__call__(), r())
        self.assertEqual(r.__call__(), r.__call__())
        self.assertEqual(r(), r())
        self.assertEqual(r(), r.__call__())
        self.assertEqual(r.__call__(), r())
        f = None
        self.assertEqual(r(), None)
        self.assertEqual(r.__call__(), None)
        self.assertEqual(r(), r())
        self.assertEqual(r(), r.__call__())
        self.assertEqual(r.__call__(), r())

    def test_callback(self):
        f
