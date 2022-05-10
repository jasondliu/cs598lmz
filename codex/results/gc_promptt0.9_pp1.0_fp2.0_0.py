import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable() working on weakref objects in cycles.

done = object()
class W(object):
    pass

def foo(obj):
    obj = weakref.ref(obj, foo)
    if obj() is not done:
        W()

def test():
    w = W()
    w.attr = w
    foo(w)

    w = None
    gc.collect()
    # w should have been collected, and shouldn't be considered unreachable
    assert not gc.collectable(W)

    ww = W()
    foo(ww)
    del ww
    gc.collect()
    # w should have been collected, and shouldn't be considered unreachable
    assert not gc.collectable(W)

    w = W()
    w.attr = w
    foo(w)
    del w
    gc.collect()
    # w should have been collected, and shouldn't be considered unreachable
    assert not gc.collectable(W)

    w = W()
    w.attr = w
    foo(w)
    foo
