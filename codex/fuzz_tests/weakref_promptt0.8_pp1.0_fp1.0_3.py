import weakref
# Test weakref.ref() with method objects.
class Foo(object):

    def f(self):
        pass


class Bar(object):

    @classmethod
    def f(cls):
        pass


def f():
    pass


class WeakRefTest(unittest.TestCase):

    def test_weakref_instancemethod(self):

        class Foo(object):

            def method(self, arg):
                pass

        o = Foo()
        foo_ref = weakref.ref(o)
        m = o.method
        self.assertIsInstance(m, types.MethodType)
        r = weakref.ref(m)
        self.assertIsInstance(r, weakref.ReferenceType)
        foo = foo_ref()
        self.assertIs(r(), m)
        self.assertIs(r().__self__, foo)
        del o
        self.assertIsNone(foo_ref())
        self.assertIsNone(r())

    def test_weakref_simple(self):
        self.assertTrue(weakref.ref(Foo().f)
