import weakref
# Test weakref.ref()
#
# This test is derived from the test case for weakref.ref() in
# Lib/test/test_weakref.py.

import gc
import unittest
from test import support

class C(object):
    pass

class D(object):
    pass

class E(C):
    pass

class F(D):
    pass

class G(E, F):
    pass

class H(C, D):
    pass

class I(H, G):
    pass

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        o = C()
        p = weakref.ref(o)
        self.assertEqual(p(), o)
        self.assertEqual(p.__class__, weakref.ReferenceType)
        o2 = C()
        p2 = weakref.ref(o2)
        self.assertNotEqual(p, p2)
        self.assertEqual(p2(), o2)
        self.assertEqual(p2.
