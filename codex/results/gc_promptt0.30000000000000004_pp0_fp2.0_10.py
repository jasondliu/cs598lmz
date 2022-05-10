import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def test_collect():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    del f, b
    gc.collect()
    assert gc.collect() == 0

def test_collect_with_callback():
    # Test gc.collect() with callbacks
    def callback(ignored):
        raise SystemError
    gc.callbacks.append(callback)
    try:
        gc.collect()
    except SystemError:
        pass
    else:
        assert False, "expected SystemError"

def test_collect_with_finalizer():
    # Test gc.collect() with finalizers
    class Foo:
        pass
    def callback(ignored):
        raise SystemError
    gc.register(Foo(), callback)
    try:
        gc.collect()
    except SystemError:
        pass
    else:
        assert False, "expected SystemError"

def test_collect_with_
