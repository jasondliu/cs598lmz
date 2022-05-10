import weakref
# Test weakref.ref() and weakref.WeakValueDictionary
from weakref import ref
# Test weakref.WeakKeyDictionary
from weakref import WeakKeyDictionary

from unittest import TestCase, skipUnless

class Foo(object):
    pass

class FooSubclass(Foo):
    pass

class WeakRefTests(TestCase):
    # we're using raw weakrefs, not the proxy objects, so we
    # can't automatically close over self.
    def get_a(self):
        return Foo()
    def get_b(self):
        return Foo()
    def get_a_subclass(self):
        return FooSubclass()

    def test_basic(self):
        o = self.get_a()
        wr = ref(o, self.callback)
        self.assertIs(wr(), o)
        self.assertEqual(wr.callback, self.callback)
        self.assertIs(wr.proxy(), o)
        self.assertTrue(wr.alive)
        del o
        self.assertFalse(wr.alive)

