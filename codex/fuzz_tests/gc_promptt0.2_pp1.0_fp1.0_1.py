import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f
gc.collect()

# Test gc.get_objects()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f
gc.collect()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f
gc.collect()

# Test gc.get_referents()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f
gc.collect()

# Test gc.is_tracked()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f
gc.collect()

# Test gc.set_threshold()

class
