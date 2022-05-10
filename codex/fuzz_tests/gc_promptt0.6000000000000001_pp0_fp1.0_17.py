import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class TestGC(unittest.TestCase):

    def test_gc(self):
        # Check that gc.collect() works
        class A:
            pass
        class B(A):
            pass
        x = A()
        x.b = B()
        x.b.a = x
        x = None
        gc.collect()

    def test_count(self):
        # Check that gc.get_count() works
        gc.collect()
        l0, l1, l2 = gc.get_count()
        class A:
            pass
        class B(A):
            pass
        x = A()
        x.b = B()
        x.b.a = x
        gc.collect()
        # We should have collected one level 0 object and two level 1 objects
        self.assertEqual(gc.get_count(), (l0+1, l1+2, l2))

    def test_threshold(self):
        # Check that gc.get_threshold() and gc.set_
