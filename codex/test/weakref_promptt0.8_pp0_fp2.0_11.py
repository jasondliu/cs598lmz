import weakref
# Test weakref.ref
import unittest
import pickle
from test import test_support

def target():
    return 42

class BasicTestCase(unittest.TestCase):

    def assertIs(self, v1, v2):
        self.assertTrue(v1 is v2, "%r is %r" % (v1, v2))

    def assertIsNot(self, v1, v2):
        self.assertTrue(v1 is not v2, "%r is not %r" % (v1, v2))

    def test_basic(self):
        # Create a weak reference to a pair
        p = (10, 20, [30, 40])
        wp = weakref.ref(p)

        # Create a weak reference to a cycle
        x = wp
        y = [wp, wp]
        del p, wp

        # Check the Python api
        self.assertTrue(x() is y[0]())
        self.assertTrue(x() is y[1]())
        self.assertFalse(x is y)
