import weakref
# Test weakref.ref()

import weakref
import unittest

class X(object):
    def __init__(self, a):
        self.a = a

class BasicTestCase(unittest.TestCase):

    def test_basic(self):
        x = X(1)
        y = X(2)
        xref = weakref.ref(x)
        xis = xref()
        self.assertEqual(xis, x)
        self.assertEqual(x.a, 1)
        self.assertEqual(xis.a, 1)
        x.a = 42
        self.assertEqual(x.a, 42)
        self.assertEqual(xis.a, 42)
        xis.a = 108
        self.assertEqual(x.a, 108)
        #
        xis2 = weakref.ref(x)
        self.assert_(xref is xis2)
        self.assertEqual(xis, xis2())
        #
        del x
