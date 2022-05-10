import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    o = Foo()
    o.x = o
    wr = weakref.ref(o)
    del o
    gc.collect()
    assert wr() is None

bar()

# Test gc.garbage

class Foo:
    pass

def bar():
    o = Foo()
    o.x = o
    wr = weakref.ref(o)
    del o
    gc.collect()
    assert wr() is None
    assert gc.garbage == []

bar()

# Test gc.get_referrers()

class Foo:
    pass

def bar():
    o = Foo()
    o.x = o
    wr = weakref.ref(o)
    del o
    gc.collect()
    assert wr() is None
    assert gc.get_referrers(Foo) == []

bar()

# Test gc.get_referents()

class Foo:
    pass

def bar():
   
