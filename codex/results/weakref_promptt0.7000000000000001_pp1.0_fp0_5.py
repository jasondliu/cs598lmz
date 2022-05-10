import weakref
# Test weakref.ref
import gc

from test import support

class C:
    pass

def target(*args):
    pass

class TestWeakref(unittest.TestCase):
    def test_basic(self):
        c = C()
        r = weakref.ref(c)
        self.assertEqual(r(), c)
        self.assertEqual(r.__class__, weakref.ref)
        self.assertEqual(r(), c)
        self.assertEqual(r.__class__, weakref.ref)

    def test_new_weakref(self):
        c = C()
        r = weakref.new(C)
        r.__init__(c)
        self.assertEqual(r(), c)
        self.assertEqual(r.__class__, weakref.ref)
        self.assertEqual(r(), c)
        self.assertEqual(r.__class__, weakref.ref)

    def test_new_weakref_exception(self):
        self.assertRaises(Type
