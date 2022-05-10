import weakref
# Test weakref.ref() and weakref.proxy()

class MyObject(object):
    pass

class WeakRefTestCase(unittest.TestCase):
    def test_weakref_ref(self):
        obj = MyObject()
        r = weakref.ref(obj)
        self.assertIsInstance(r, weakref.ref)
        self.assertIs(obj, r())

    def test_weakref_proxy(self):
        obj = MyObject()
        r = weakref.proxy(obj)
        self.assertIsInstance(r, weakref.ProxyTypes)
        self.assertIs(obj, r)

    def test_weakref_proxy_callable(self):
        # Issue #14674: weakref.proxy(obj) should be callable
        # if obj is callable.
        class Callable(object):
            def __call__(self):
                pass
        c = Callable()
        p = weakref.proxy(c)
        self.assertTrue(callable(p))
        self.assertEqual(p(), None)

