import weakref
# Test weakref.ref() and weakref.proxy()

from test import support
#from test.test_support import run_unittest
from test.support import run_unittest

class Foo:
    pass

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        # Test a simple creation of a weak reference and dereferencing it
        f = Foo()
        f.a = 10
        f.b = 20
        p = weakref.proxy(f)
        self.assertEqual(f.a, 10)
        self.assertEqual(f.b, 20)
        self.assertEqual(p.a, 10)
        self.assertEqual(p.b, 20)
        self.assertTrue(f.__class__ is Foo)
        self.assertTrue(p.__class__ is Foo)
        self.assertTrue(p.__class__ is f.__class__)

    def test_callable(self):
        # Test that proxies are callable if the referent is callable
        def f():
           
