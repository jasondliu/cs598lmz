import weakref
# Test weakref.ref()
import gc

def f():
    return 42

def test_ref():
    o = f()
    r = weakref.ref(o)
    assert r() == 42
    del o
    gc.collect()
    assert r() == 42

def test_callable_ref():
    o = f
    r = weakref.ref(o)
    assert r() == f
    del o
    gc.collect()
    assert r() == f

def test_bound_method_ref():
    class A:
        def __init__(self):
            self.x = 42
        def f(self):
            return self.x
    a = A()
    o = a.f
    r = weakref.ref(o)
    assert r()() == 42
    del a, o
    gc.collect()
    assert r()() == 42

def test_unbound_method_ref():
    class A:
        def __init__(self):
            self.x = 42
        def f(self):
            return
