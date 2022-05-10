import weakref
# Test weakref.ref
import unittest
from test import support
class TestKeyedRef(unittest.TestCase):

    def test_basic(self):
        for base in object, int:
            class C(base):
                pass
            obj = C()
            obj.foo = 42
            keyed_ref = weakref.KeyedRef(obj, 'foo')
            self.assertIs(keyed_ref(), obj)
            self.assertEqual(keyed_ref(), 42)
            del obj
            gc.collect()
            self.assertIsNone(keyed_ref())

    def test_callable(self):
        class C:
            pass
        obj = C()
        obj.foo = 42
        keyed_ref = weakref.KeyedRef(obj, lambda : 'foo')
        self.assertIs(keyed_ref(), obj)
        self.assertEqual(keyed_ref(), 42)
        del obj
        gc.collect()
        self.assertIsNone(keyed_ref())

