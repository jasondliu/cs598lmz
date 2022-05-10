import gc, weakref
import sys
import types
import unittest

class TestWeakref(unittest.TestCase):
    # Additional test cases can be found in the reference test case
    # library, Lib/test/test_weakref.py

    def test_basic(self):
        o = C()
        p = C()
        q = C()
        r = C()
        o.x = p
        o.y = q
        p.x = q
        p.y = r
        q.x = r
        q.y = o
        r.x = p
        r.y = q
        wr = weakref.ref(o)
        self.assertEqual(wr(), o)
        self.assertEqual(wr().x, p)
        self.assertEqual(wr().y, q)
        self.assertEqual(wr().x.x, q)
        self.assertEqual(wr().x.y, r)
        self.assertEqual(wr().y.x, r)
