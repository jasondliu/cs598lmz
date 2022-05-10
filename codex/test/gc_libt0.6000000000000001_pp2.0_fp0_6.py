import gc, weakref
from _weakrefset import WeakSet
from unittest import TestCase, TestSuite, makeSuite, main

class X(object):
    pass

class TestWeakSet(TestCase):
    def test_basics(self):
        s = WeakSet()
        self.assertEqual(len(s), 0)
        x = X()
        s.add(x)
        self.assert_(x in s)
        self.assertEqual(len(s), 1)
        y = X()
        s.add(y)
        self.assert_(y in s)
        self.assert_(x in s)
        self.assertEqual(len(s), 2)
        del x
        gc.collect()
        self.assert_(y in s)
        self.assertEqual(len(s), 1)
        del y
        gc.collect()
        self.assertEqual(len(s), 0)

    def test_len_during_iteration(self):
        s = WeakSet()
        x = X()
