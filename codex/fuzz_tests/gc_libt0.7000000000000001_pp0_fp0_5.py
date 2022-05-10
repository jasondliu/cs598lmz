import gc, weakref
from weakref import ref as weakref_ref
from weakref import WeakKeyDictionary, WeakValueDictionary

import py

class TestWeakref(object):
    def test_basics(self):
        def callback(r):
            pass
        x = object()
        x_r = weakref.ref(x, callback)
        assert x_r() is x
        del x
        assert x_r() is None
        assert x_r() is None
        gc.collect()
        assert x_r() is None

    def test_weakref(self):
        x = object()
        x_r = weakref.ref(x)
        assert x_r() is x
        del x
        gc.collect()
        assert x_r() is None

    def test_unboundmethod(self):
        class A(object):
            def f(self):
                pass
        a = A()
        a.f()
        a_f = a.f
        assert a_f
        del a
        gc.collect()
        assert a_
