import gc, weakref

def test_weakref_to_method():
    # Issue1188090: Weak references to bound methods should be supported.
    class C(object):
        def foo(self): pass
    c = C()
    ref = weakref.ref(c.foo)
    del c
    gc.collect()
    assert ref() is None

def test_finalizer_newstyle():
    # Issue1188090: Weak references to bound methods should be supported.
    class C(object):
        def foo(self): pass
    c = C()
    f = finalize(c, c.foo)
    f.detach()
    del c
    gc.collect()
    assert f.alive

def test_finalizer_oldstyle():
    # Issue1188090: Weak references to bound methods should be supported.
    class C:
        def foo(self): pass
    c = C()
    f = finalize(c, c.foo)
    f.detach()
    del c
    gc.collect()
    assert f.alive


