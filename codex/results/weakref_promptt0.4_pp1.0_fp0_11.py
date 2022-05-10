import weakref
# Test weakref.ref()
#
# Create a weakref to an object
import os
import gc
import weakref
import unittest
from test import support

class Foo(object):
    pass

class TestWeakref(unittest.TestCase):
    def test_builtin_types(self):
        # Test weak references to builtin types
        s = "hello"
        wr = weakref.ref(s)
        self.assertEqual(wr(), s)
        s2 = wr()
        self.assertEqual(s2, s)
        del s
        gc.collect()
        self.assertEqual(wr(), s2)
        del s2
        gc.collect()
        self.assertEqual(wr(), None)

    def test_builtin_types_with_cyclic_dict(self):
        # Test weak references to builtin types
        s = "hello"
        d = {}
        d[1] = d
        wr = weakref.ref(s, lambda *args: d.clear())
        self.assertEqual(wr(),
