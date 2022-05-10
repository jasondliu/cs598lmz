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

l = gc.get_objects()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

l = gc.get_referrers(f)

# Test gc.get_referents()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

l = gc.get_referents(f)

# Test gc.get_threshold()

gc.get_threshold()

# Test gc.set_threshold()

gc.set_threshold(700, 10, 5)
gc.
