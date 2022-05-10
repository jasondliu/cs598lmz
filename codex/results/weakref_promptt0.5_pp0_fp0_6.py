import weakref
# Test weakref.ref(None)
with self_test():
    ref = weakref.ref(None)
    assert ref() is None
    assert ref() is None

# Test weakref.ref(object)
with self_test():
    o = object()
    ref = weakref.ref(o)
    assert ref() is o
    assert ref() is o
    del o
    assert ref() is None
    assert ref() is None

# Test weakref.ref(callable)
with self_test():
    def f():
        pass
    ref = weakref.ref(f)
    assert ref() is f
    assert ref() is f
    del f
    assert ref() is None
    assert ref() is None

# Test weakref.ref(object, callback)
with self_test():
    o = object()
    called = False
    def callback(ref):
        nonlocal called
        called = True
    ref = weakref.ref(o, callback)
    assert not called
    assert ref() is o
    assert ref() is o
    del o
    assert
