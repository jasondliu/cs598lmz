import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() during iteration.
# Previous versions of Python called tp_clear() at unexpected times,
# crashing in the case of extension types with dynamically allocated
# cross-referenced internal state.  See SF bug #509563.

import unittest

class TestGcCollectable(unittest.TestCase):

    def test_basic(self):

        class C(object):
            pass

        c = C()
        wr = weakref.ref(c)
        c.foo = c
        del c
        gc.collect()
        self.assertIsNone(wr())

    def test_basic_with_finalizer(self):

        class C(object):
            pass

        c = C()
        wr = weakref.ref(c, lambda c=c: c.foo)
        c.foo = c
        del c
        gc.collect()
        self.assertIsNone(wr())

    def test_basic_with_finalizer2(self):

        class C(object):
            pass

        c = C()
        wr = weakref.ref(
