import weakref
# Test weakref.ref() for callable objects.
import sys
import test.test_support
import unittest


class C:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self):
        return self.arg

class CallableRefTestCase(unittest.TestCase):

    def test(self):
        a = C(42)
        b = weakref.ref(a)
        a2 = b()
        self.assertEqual(a2(), 42)
        del a
        self.assertEqual(b(), None)
        self.assertEqual(b() is None, True)
        self.assertEqual(b() == None, True)
        self.assertEqual(b() is not None, False)
        self.assertEqual(b() != None, False)

    def test_callable_ref_subclass(self):
        class MyRef(weakref.ref):
            def __call__(self):
                return 'hello'
        a = C(42)
