import weakref
# Test weakref.ref() and weakref.proxy()

import sys
import weakref
import unittest
from test import test_support

#
# Basic sanity tests
#

class Foo:
    pass

class BasicTestCase(unittest.TestCase):

    def test_basic(self):
        foo = Foo()
        foo_ref = weakref.ref(foo)
        foo_proxy = weakref.proxy(foo)

        self.assertEqual(foo_ref(), foo)
        self.assertEqual(foo_proxy, foo)

        del foo
        self.assertEqual(foo_ref(), None)
        self.assertRaises(ReferenceError, getattr, foo_proxy, 'whatever')

    def test_callable(self):
        foo = Foo()
        foo_ref = weakref.ref(foo)
        self.assert_(callable(foo_ref))
        self.assertEqual(foo_ref(), foo)
        self.assertEqual(foo_ref(), foo)
        self.assertEqual(foo_ref(), foo)
        del foo
