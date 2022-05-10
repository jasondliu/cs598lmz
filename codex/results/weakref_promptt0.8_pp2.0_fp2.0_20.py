import weakref
# Test weakref.ref(a,b)
import unittest
import gc
class G():
    pass

class H(object):
    pass

class WeakRefTest(unittest.TestCase):

    def callback(self, arg):
        self.callback_arg = arg

    def test_basic(self):
        o = G()
        r = weakref.ref(o)
        self.assertTrue(r() is o)
        del o
        gc.collect()
        self.assertTrue(r() is None)

    def test_basic_newstyle(self):
        o = H()
        r = weakref.ref(o)
        self.assertTrue(r() is o)
        del o
        gc.collect()
        self.assertTrue(r() is None)

    def test_callable(self):
        o = G()
        self.assertEqual(o(), 42)
        r = weakref.ref(o)
        self.assertTrue(r() is o)
        del o
        gc.collect()
        self.assert
