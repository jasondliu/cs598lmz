import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def test_collect():
    class A:
        pass
    a = A()
    a.b = A()
    a.b.a = a
    a.b.b = a.b
    ref = weakref.ref(a)
    assert ref() is a
    del a
    gc.collect()
    assert ref() is None

# Test gc.garbage
def test_garbage():
    class A:
        pass
    a = A()
    a.b = A()
    a.b.a = a
    a.b.b = a.b
    ref = weakref.ref(a)
    assert ref() is a
    del a
    gc.collect()
    assert ref() is None
    assert gc.garbage
    del gc.garbage[:]

# Test gc.get_objects()
def test_get_objects():
    class A:
        pass
    a = A()
    a.b = A()
    a.b.a = a
    a.b.b =
