import weakref
# Test weakref.ref objects to functions and classes.
import operator
import pickle
import unittest
import copy_reg


class Foo(object):
    pass


class CallableWeakrefTestCase(unittest.TestCase):
    def setUp(self):
        self.foo = Foo()
        self.foo.f = Foo()
        self.foo.f.f = self.foo

    def test_foo(self):
        self.assertTrue(callable(self.foo.f))
        self.assertTrue(callable(self.foo.f.f))
        self.assertTrue(callable(self.foo))

    def test_constructor(self):
        self.assertRaises(TypeError, weakref.ref, self.foo, Foo)
        self.assertRaises(TypeError, weakref.ref, self.foo, self.foo)
        self.assertRaises(TypeError, weakref.ref, self.foo, self.foo)
        self.assertRaises(TypeError, weakref.ref, self.foo.f, self.foo.f)

