import weakref

from .. import _base


class TestWeakMethod(unittest.TestCase):

    def test_weak_method(self):
        class A:
            def f(self):
                pass
        a = A()
        cb = weakref.WeakMethod(a.f)
        self.assertEqual(cb(), None)
        del a
        self.assertEqual(cb(), None)
        self.assertEqual(cb(), None)

    def test_weak_method_call(self):
        class A:
            def f(self):
                return self
        a = A()
        cb = weakref.WeakMethod(a.f)
        self.assertEqual(cb(), a)
        del a
        self.assertEqual(cb(), None)
        self.assertEqual(cb(), None)

    def test_weak_method_call_args(self):
        class A:
            def f(self, x, y):
                return (self, x, y)
        a = A()
        cb = weakref.WeakMethod
