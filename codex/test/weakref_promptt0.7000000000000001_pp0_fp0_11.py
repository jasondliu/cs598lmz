import weakref
# Test weakref.ref(object)
from test.test_support import run_unittest
from test import test_support

class Foo(object):
    pass

class MyWeakref(object):
    def __init__(self, arg):
        self.ref = weakref.ref(arg)
        self.arg = arg

    def __call__(self):
        return self.ref()

class HashCmp(object):
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value

class WeakrefTestCase(unittest.TestCase):
    def test_basic(self):
        f = Foo()
        p = weakref.proxy(f)
        self.assertEqual(f, p)
        self.assertEqual(p, f)
        self.assertEqual(p.__class__, Foo)
        self.assertEqual(type(p), Foo)
