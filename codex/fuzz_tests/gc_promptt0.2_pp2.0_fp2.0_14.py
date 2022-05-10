import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    gc.collect()
    assert wr() is None

bar()

# Test gc.garbage

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    gc.collect()
    assert wr() is None

bar()

# Test gc.get_objects()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    gc.collect()
    assert wr() is None

bar()

# Test gc.get_referrers()

class Foo:
    pass

def bar():
    f = Foo()
    wr = weakref.ref(f)
    del f
    gc.collect()
    assert wr() is None

bar()

# Test gc.get_referents()
