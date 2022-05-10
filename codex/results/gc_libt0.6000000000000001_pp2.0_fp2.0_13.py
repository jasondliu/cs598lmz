import gc, weakref
from contextlib import contextmanager

class C(object):
    pass

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

class GCTest(unittest.TestCase):
    def test_basics(self):
        gc.set_debug(gc.DEBUG_STATS)
        gc.collect()
        self.assertEqual(gc.get_count(), (0, 0, 0))
        self.assertTrue(gc.isenabled())
        gc.disable()
        self.assertFalse(gc.isenabled())
        gc.enable()
        self.assertTrue(gc.isenabled())
        gc.set_threshold(500)
        self.assertEqual(gc.get_threshold(), 500)

    def test_collect(self):
        class C:
            pass
        c = C()
        c.a = C()
        c.a.b = c
        ref = weakref.ref(c)
        del c
        for i in range(
