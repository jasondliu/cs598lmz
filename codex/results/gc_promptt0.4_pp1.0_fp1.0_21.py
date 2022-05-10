import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

import unittest
from test import support

class GCTestCase(unittest.TestCase):
    def setUp(self):
        self.old_debug = gc.get_debug()
        self.old_threshold = gc.get_threshold()
        gc.set_debug(gc.DEBUG_STATS)
        gc.enable()

    def tearDown(self):
        gc.set_debug(self.old_debug)
        gc.set_threshold(*self.old_threshold)

    def test_collect(self):
        # Create a cycle with a length that is a multiple of the cycle
        # detector's cycle length
        l = []
        for i in range(24):
            l = [l, i]
        del l
        gc.collect()
        self.assertEqual(gc.garbage, [])

    def test_collect_generations(self):
        # Create a cycle with a length that is a multiple of the cycle
        # detector's cycle length
        l = []
        for i
