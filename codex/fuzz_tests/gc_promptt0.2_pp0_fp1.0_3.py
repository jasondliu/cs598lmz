import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = f
    del f

bar()
gc.collect()

# Test gc.get_referrers()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = f
    del f

bar()
gc.collect()

# Test gc.get_referents()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = f
    del f

bar()
gc.collect()

# Test gc.get_objects()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = f
    del f

bar()
gc.collect()

# Test gc.get_stats()

gc.collect()

# Test gc.set_debug()

gc.set_debug(gc.DEBUG_STATS)
gc.collect()
gc.set_debug(gc.DEBUG_LEAK
