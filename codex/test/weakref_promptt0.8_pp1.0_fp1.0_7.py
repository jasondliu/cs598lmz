import weakref
# Test weakref.ref foo(x) syntax
import weakref
import unittest
import copy
import pickle
from test import support
class Foo:
    pass
class CallKeyTestCase(unittest.TestCase):

    def callback(self, arg):
        self.called = 1

    def test_call_key(self):
        f = Foo()
        w = weakref.ref(f, self.callback)
        self.called = 0
        f2 = w()
        self.assertIs(f, f2)
        self.assertEqual(self.called, 0)
        del f
        support.gc_collect()
        self.assertEqual(self.called, 1)

    def test_called_on_underlying_object_deletion(self):
        class Foo:
            def __init__(self):
                self.f = Foo()
        f = Foo()
        w = weakref.ref(f.f, self.callback)
        self.called = 0
        del f
        support.gc_collect()
