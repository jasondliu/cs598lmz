import gc, weakref


class TestDeleted(unittest.TestCase):
    def test_deleted(self):
        def del_callback(self_ref):
            nonlocal self_ref_callback
            self_ref_callback = self_ref

        self_ref_callback = None

        self_ref = weakref.ref(self, del_callback)
        del_self = self_ref()

        self.assertIs(del_self, self)
        self.assertIs(self_ref(), self)
        self.assertIsNone(self_ref_callback)

        self = None
        gc.collect()
        self.assertIs(del_callback.__func__, del_callback)
        self.assertIs(del_self, self_ref())
        self.assertIs(self_ref_callback(), del_self)
        self.assertIs(del_self, None)


class TestProxyDeleted(unittest.TestCase):
    def test_deleted(self):
        o = object()
        p = weakref.proxy(o)
        self.assertIs
