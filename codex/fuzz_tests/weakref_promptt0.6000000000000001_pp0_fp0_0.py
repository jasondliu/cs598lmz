import weakref
# Test weakref.ref(x) == weakref.ref(x)
import unittest
class C(object):
    pass
class D(object):
    pass
class E(object):
    pass
class TestWeakrefEquality(unittest.TestCase):
    def test_basic(self):
        c1 = C()
        c2 = C()
        self.assertEqual(weakref.ref(c1), weakref.ref(c1))
        self.assertNotEqual(weakref.ref(c1), weakref.ref(c2))
        self.assertNotEqual(weakref.ref(c1), c1)
        self.assertNotEqual(c1, weakref.ref(c1))
    def test_subclass(self):
        c1 = C()
        d1 = D()
        d2 = D()
        self.assertNotEqual(weakref.ref(c1), weakref.ref(d1))
        self.assertNotEqual(weakref.ref(d1), weakref.ref(d2))
    def test
