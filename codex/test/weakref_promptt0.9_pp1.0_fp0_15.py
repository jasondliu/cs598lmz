import weakref
# Test weakref.ref()
class TestCallback(unittest.TestCase):
    def callback(self, ref, value):
        self.called = True

    def test_ref(self):
        a = weakref.ref(42, self.callback)
        self.called = False
        self.assertEqual(a(), 42)
        a = None
        gc.collect()
        if self.called:
            a = 42
        else:
            a = 1
        self.assertEqual(a, 42)
    if hasattr(sys, "gettotalrefcount"):
        def test_getweakrefcount(self):
            # test _PyWeakref_GetWeakrefCount()
            class Foo(object):
                pass

            a = Foo()
            a.b = weakref.ref(a)
            self.assertEqual(sys.getrefcount(a), 3)
            weakref.ref(a)
            del a
            gc.collect()
    def test_callback_with_args(self):
        self.called = []
