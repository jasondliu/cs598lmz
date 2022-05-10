import weakref
# Test weakref.ref() against a custom class
import unittest


class Foo:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Foo(%s)' % self.name


class WeakRefTest(unittest.TestCase):

    def test_basic(self):
        o = Foo('an object')
        r = weakref.ref(o)
        p = weakref.proxy(o)
        self.assertEqual(r(), o)
        self.assertEqual(p, o)
        o2 = r()
        self.assertEqual(o, o2)
        o3 = p
        self.assertEqual(o, o3)

    def test_hash(self):
        o = Foo('an object')
        r = weakref.ref(o)
        p = weakref.proxy(o)
        self.assertEqual(hash(o), hash(r))
        self.assertEqual(hash(o), hash(p))
        d = {}
        d[
