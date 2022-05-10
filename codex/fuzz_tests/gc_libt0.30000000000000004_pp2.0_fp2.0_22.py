import gc, weakref
from _weakrefset import WeakSet
from _weakref import proxy
from _weakref import CallableProxyType, ProxyType
from _weakref import getweakrefcount, getweakrefs

import unittest
from test import test_support

class TestWeakSet(unittest.TestCase):

    def test_basic(self):
        s = WeakSet()
        self.assertEqual(len(s), 0)
        self.assertRaises(KeyError, s.remove, 42)
        s.add(frozenset([1]))
        self.assertEqual(len(s), 1)
        s.remove(frozenset([1]))
        self.assertEqual(len(s), 0)
        s.add(frozenset([1]))
        self.assertEqual(len(s), 1)
        s.discard(frozenset([1]))
        self.assertEqual(len(s), 0)
        s.discard(frozenset([1]))
        self.assertEqual(len
