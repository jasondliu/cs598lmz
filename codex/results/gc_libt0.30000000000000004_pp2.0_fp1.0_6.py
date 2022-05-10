import gc, weakref
from . import _pytest

class TestWeakRef:
    def test_weakref_basic(self):
        l = []
        def remove(x):
            l.append(x)
        a = weakref.ref(remove, l.append)
        assert l == []
        del remove
        gc.collect()
        assert l == [a]
        assert a() is None

    def test_weakref_callbacks(self):
        l = []
        def remove(x):
            l.append(x)
        a = weakref.ref(remove, l.append)
        b = weakref.ref(remove, l.append)
        del remove
        gc.collect()
        assert l == [a, b]
        assert a() is None
        assert b() is None

    def test_weakref_callbacks_remove(self):
        l = []
        def remove(x):
            l.append(x)
        a = weakref.ref(remove, l.append)
        b = weakref.ref(remove, l.append
