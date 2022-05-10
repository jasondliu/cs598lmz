import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class test_gc_collect(unittest.TestCase):
    def setUp(self):
        self.l = list(range(10))
    def test_collect(self):
        gc.collect()
        self.assertTrue(gc.collect())
    def test_garbage(self):
        self.l = 1   # self.l is now garbage
        self.assertTrue(gc.collect())
    def test_uncollectable(self):
        l = self.l
        del self.l
        self.assertFalse(gc.collect())
    def test_del_cycles(self):
        l = self.l
        l.append(l)
        self.assertFalse(gc.collect())
    def test_no_free_lists(self):
        for k in range(10000):
            x = []
            x.append(x)
        gc.collect()
        self.assertFalse(gc.collect())

# Test the generational GC
class test_gc_generational(unittest.TestCase):
    def setUp(self):

