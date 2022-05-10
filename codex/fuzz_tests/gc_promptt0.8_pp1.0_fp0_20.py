import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
def take_ref(r):
    print("Took a ref to", r)
def test():
    obj = object()
    ref = weakref.ref(obj, take_ref)
    assert gc.is_tracked(obj)
    del obj
    for i in range(3):
        gc.collect()
        assert not gc.is_tracked(ref())
test()
# Test gc.get_objects()
def test():
    obj = object()
    gc.collect()
    # A newly created object is obviously tracked
    assert obj in gc.get_objects()
    # But a deleted object is not
    del obj
    gc.collect()
    # But a deleted object is not
    assert obj not in gc.get_objects()
test()
# Test gc.get_stats()
def test():
    obj = object()
    gc.collect()
    # A newly created object is obviously tracked
    assert obj in gc.get_objects()
    # But a deleted object is not
    del obj
   
