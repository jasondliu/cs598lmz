import weakref
# Test weakref.ref() and weakref.proxy().

import sys
import unittest
import weakref

class Foo(object):
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return '<Foo(%r) object at %#x>' % (self.arg, id(self))


class TestWeakref(unittest.TestCase):

    def assertEqual(self, x, y):
        self.assertTrue(x == y)
    def assertNotEqual(self, x, y):
        self.assertTrue(x != y)

    def test_basic(self):
        self.assertTrue(weakref.ref is weakref.ReferenceType)
        self.assertTrue(weakref.proxy is weakref.ProxyType)

    def test_ref(self):
        f = Foo('my arg')
        r = weakref.ref(f)
        self.assertEqual(r(), f)
        self.assertEqual(r.arg, f.arg)
        self.assertEqual
