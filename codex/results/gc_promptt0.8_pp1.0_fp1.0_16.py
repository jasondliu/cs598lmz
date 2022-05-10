import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() versus del
class TestGC(unittest.TestCase):
    def test_del(self):
        gcpolicy = gc.get_threshold()
        try:
            gc.set_threshold(0)
            # Create a cycle.
            x = MyObj()
            x.cycle = x
            y = MyObj()
            y.cycle = y
            x.child = y
            del x, y
            # Now break the cycle, but don't del x.
            gc.collect()
            self.assertEqual(MyObj.alive, 0)
        finally:
            gc.set_threshold(*gcpolicy)
class TestWeakRef(unittest.TestCase):
    def test_basic_weak_ref(self):
        # Try a weak reference
        x = MyObj()
        d = weakref.WeakValueDictionary()
        d['obj'] = x
        self.assertEqual(d['obj'].__class__, MyObj)
        del x
        gc.collect()
        self.assertEqual
