import weakref
# Test weakref.ref() with a callable object that is not weakly referenceable.
import unittest
import gc

class Callable:
    def __init__(self, obj):
        self.obj = obj
    def __call__(self):
        return self.obj

class TestWeakref(unittest.TestCase):

    def test_callable(self):
        obj = Callable(42)
        ref = weakref.ref(obj)
        self.assertEqual(ref(), obj)
        del obj
        self.assertEqual(ref(), 42)
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())
        self.assertEqual(ref(), ref())

