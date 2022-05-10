import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and del

import sys
from test.test_support import run_unittest, check_impl_detail


class GCTest(unittest.TestCase):

    def test_simple_cycles(self):
        # This is the most simple cycle:  one object references another.
        # They are collected right away.
        x = []
        x.append(x)
        del x
        # Now a slightly larger cycle.
        x = []
        y = [x]
        x.append(y)
        del x, y
        # Now a slightly larger cycle with a edge case.
        x = []
        y = [x]
        x.append(y)
        u = []
        v = []
        w = []
        y.append(u)
        y.append(v)
        y.append(w)
        y.append(y)
        del x, y, u, v, w
        # A self-referent list that isn't part of a cycle.
        x = []
        x.append(x)
        del x

