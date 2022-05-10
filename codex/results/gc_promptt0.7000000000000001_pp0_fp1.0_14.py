import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage at level 1
#
# Make sure the objects in gc.garbage are really unreachable
# and that no additional unreachable objects are missed.

import unittest
from test import test_support
from gc import collect as gc_collect
from gc import collect as gc_collect1
from gc import collect as gc_collect2
from gc import collect as gc_collect3
from weakref import ref

class GCTest(unittest.TestCase):
    # Constructor.  Remember the original collect function.
    def setUp(self):
        self.original_collect = gc.collect
        self.was_debug = gc.get_debug()
        self.assertEqual(gc.get_threshold(), (700, 10, 10))
        self.old_thresholds = gc.get_threshold()
        gc.set_threshold(42)
        gc.set_debug(0)
        gc.collect()
        self.t = None
        self.f = None

    #
