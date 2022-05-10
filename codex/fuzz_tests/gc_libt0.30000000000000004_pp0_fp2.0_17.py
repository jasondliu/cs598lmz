import gc, weakref
import sys
import unittest

from test import support

# Base class for testing weakrefable objects.
class Weakrefable:
    def test_basic(self):
        o = self.thetype('spam')
        p = weakref.proxy(o)
        self.assertEqual(o.foo, 'spam')
        self.assertEqual(p.foo, 'spam')
        o.foo = 'ham'
        self.assertEqual(o.foo, 'ham')
        self.assertEqual(p.foo, 'ham')
        o.bar = 'eggs'
        self.assertEqual(o.bar, 'eggs')
        self.assertEqual(p.bar, 'eggs')
        self.assertEqual(p.foo, 'ham')
        self.assertEqual(o.foo, 'ham')
        self.assertEqual(p.__class__, weakref.ProxyType)
        self.assertEqual(type(p), weakref.ProxyType)
        self.assertEqual(p.
