import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, gc.is_tracked, and gc.get_referrers

import unittest

class GCTests(unittest.TestCase):
    def test_basics(self):
        # Check simple tracking and untracking.
        a = []
        self.assertTrue(gc.is_tracked(a))
        del a
        gc.collect()
        b = []
        b.append(b)
        self.assertTrue(gc.is_tracked(b))
        b = None
        gc.collect()
        self.assertEqual(gc.collect(), 0)

    #def test_weakref(self):
    #    # Check that gc.collect() finds gc'ed weakrefs.
    #    class C:
    #        pass
    #    a = C()
    #    w = weakref.ref(a)
    #    del a
    #    gc.collect()
    #    b = C()
    #    self.assertIs(w(), None)
    #    self.assertTrue
