import weakref
# Test weakref.ref
import test.test_weakref
test.test_weakref.ref_test(weakref.ref)

import unittest
import weakref

class MyBaseClass(object):
    pass

class MyClass(MyBaseClass):
    pass

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        o = MyClass()
        p = weakref.ref(o)
        self.assertEqual(p(), o)
        self.assertEqual(p.__class__, weakref.ref)
        self.assertEqual(type(p), weakref.ref)
        self.assertEqual(p.__call__(), o)
        p2 = weakref.proxy(o)
        self.assertEqual(p, p2)
        self.assertEqual(p.__class__, weakref.ProxyType)
        self.assertEqual(type(p2), weakref.ProxyType)
        self.assertNotEqual(p.__class__, weakref.ref)
        self.assertE
