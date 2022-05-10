import weakref
# Test weakref.ref functions
import gc
import unittest
from test import test_support


class MyBase:
    pass

class MyKlass(MyBase):
    pass

class WeakRefTestCase(unittest.TestCase):
    def test_basic(self):
        o = MyBase()
        r = weakref.ref(o)
        self.assertEqual(o, r())

        o2 = MyBase()
        r2 = weakref.ref(o2)
        self.assertEqual(o2, r2())
        self.assertNotEqual(o, r2())

        # calling a dead ref raises TypeError
        o = None
        gc.collect()
        self.assertRaises(TypeError, r)

    def test_callback(self):
        self.callback_counter = 0
        def callback(r):
            self.callback_counter += 1
        o = MyBase()
        r = weakref.ref(o, callback)
        o = None
        gc.collect()
