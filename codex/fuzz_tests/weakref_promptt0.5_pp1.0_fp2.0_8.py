import weakref
# Test weakref.ref(instance)
# Test weakref.ref(instance, callback)
# Test weakref.proxy(instance)
# Test weakref.proxy(instance, callback)

import sys
import copy
import unittest
from test.support import run_unittest
from weakref import *

class BasicTest(unittest.TestCase):

    def test_basic(self):
        # Create a weak reference to a local object
        o = C()
        r = ref(o)
        p = proxy(o)
        self.assertEqual(o, r())
        self.assertEqual(o, p)
        del o
        self.assertIs(r(), None)
        self.assertRaises(ReferenceError, getattr, p, 'attr')

    def test_basic_callback(self):
        # Create a weak reference to a local object with a callback
        o = C()
        l = []
        def callback(arg):
            l.append(arg)
        r = ref(o, callback)
        del o
        gc.collect()
        self.
