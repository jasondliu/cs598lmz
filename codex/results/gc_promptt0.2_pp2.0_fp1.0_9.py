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

# Test gc.garbage

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f

gc.collect()

print gc.garbage

# Test gc.get_objects()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f

gc.collect()

print gc.get_objects()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

del f

gc.collect()

print gc.get_referrers(gc.garbage[0])

# Test gc.get_referents()

class Foo:
    pass

f = Foo()

