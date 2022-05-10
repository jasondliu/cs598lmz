import weakref
# Test weakref.ref()
from test import test_support
import unittest

class Foo(object):
    pass

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        f = Foo()
        p = weakref.ref(f)
        self.assertEqual(p(), f)
        self.assertEqual(p.__call__(), f)

    def test_basic_callable(self):
        f = Foo()
        def g():
            return f
        p = weakref.ref(g)
        self.assertEqual(p(), f)
        self.assertEqual(p.__call__(), f)

    def test_basic_callable_exception(self):
        def g():
            raise ValueError
        p = weakref.ref(g)
        self.assertRaises(ValueError, p)

    def test_basic_callable_arg(self):
        f = Foo()
        def g(x):
            return x
        p = weakref.ref(g)
        self.assertEqual
