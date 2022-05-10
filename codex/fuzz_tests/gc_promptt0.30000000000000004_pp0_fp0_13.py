import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo:
    pass

class Bar(Foo):
    pass

class Baz(Foo):
    pass

def test_gc_collect():
    # Create a bunch of objects, some of which are cyclic
    foo = Foo()
    foo.bar = Bar()
    foo.bar.foo = foo
    foo.bar.bar = foo.bar
    foo.baz = Baz()
    foo.baz.foo = foo
    foo.baz.bar = foo.bar
    foo.baz.baz = foo.baz
    # Create a weak reference to foo.baz
    foo_baz_ref = weakref.ref(foo.baz)
    # Get rid of foo
    del foo
    # Collect
    gc.collect()
    # Check
    assert foo_baz_ref() is None

def test_gc_collect_weakref():
    # Create a bunch of objects, some of which are cyclic
    foo = Foo()
    foo.bar = Bar()
    foo.bar.foo
