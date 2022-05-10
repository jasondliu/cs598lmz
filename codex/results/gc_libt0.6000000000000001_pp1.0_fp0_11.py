import gc, weakref

class TestWeakref(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.objs = []
        for i in range(self.n):
            obj = [i]
            self.objs.append(obj)
            wr = weakref.ref(obj)
            self.assertTrue(wr() is obj)
            self.assertTrue(wr() is not None)
        self.assertTrue(len(gc.get_objects()) >= self.n)
        self.objs = None

    def test_weakref_with_callbacks(self):
        # test weakrefs with callbacks
        self.objs = []
        callbackCalled = []
        def remove(wr, selfref=weakref.ref(self)):
            self = selfref()
            if self is not None:
                self.objs.remove(wr())
                self.assertTrue(wr() is None)
                callbackCalled.append(True)

        for i in range(self.n):
            obj = [i]

