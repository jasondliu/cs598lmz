import gc, weakref

from . import _pytest

class TestWeakref:
    def test_weakref_basic(self):
        class A:
            pass
        a = A()
        a.x = 1
        w = weakref.ref(a)
        assert w() is a
        assert w().x == 1
        del a
        gc.collect()
        assert w() is None

    def test_weakref_callback(self):
        class A:
            pass
        a = A()
        a.x = 1
        l = []
        def callback(w):
            l.append(w)
        w = weakref.ref(a, callback)
        assert w() is a
        assert w().x == 1
        del a
        gc.collect()
        assert w() is None
        assert len(l) == 1
        assert l[0]() is None

    def test_weakref_callback_exception(self):
        class A:
            pass
        a = A()
        a.x = 1
        l = []
        def callback
