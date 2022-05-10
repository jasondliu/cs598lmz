import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakref.
#
# This test is on weakrefs with callbacks and gc.collect.
#
# Based on test_weakref.py by Jason Orendorff.

import test.support, unittest, weakref

class Test(unittest.TestCase):

    def callback(self, w):
        self.callback_called = 1
        self.w_obj = w()

    def test_callback(self):
        self.callback_called = 0
        self.w_obj = None
        a = []
        w = weakref.ref(a, self.callback)
        self.assertEqual(self.callback_called, 0)
        self.assertIsNone(self.w_obj)
        del a
        gc.collect()
        self.assertEqual(self.callback_called, 1)
        self.assertIsNone(self.w_obj)

    def test_callback_during_collection(self):
        # Issue #17085: test that a callback may trigger the collection of
        # objects which are still alive when the
