import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to callables.
#
# Weakrefs to callables should be callable as long as there is a cycle
# involving the callable.

from weakref import ref, WeakKeyDictionary
from gc import collect, get_referrers

def func():
    pass

def capture(func, *args):
    def f(*args):
        return func(*args)
    return ref(f)

def test(ctx, r):
    assert r()(ctx) == ctx
    collect()
    r()(ctx)
    collect()

def test_method(ctx, r):
    assert r()(ctx) == ctx
    collect()
    r()(ctx)
    collect()

class C:
    def meth(self):
        return self

def test_instancemethod(ctx, r):
    assert r()(ctx) == ctx
    collect()
    r()(ctx)
    collect()

def test_partial(ctx, r):
    from functools import partial
    p = partial(func, ctx
