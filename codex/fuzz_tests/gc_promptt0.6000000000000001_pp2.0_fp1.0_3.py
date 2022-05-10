import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class Foo:
    pass

f = Foo()

assert gc.collectable(f)
assert gc.is_tracked(f)

# Test gc.get_referrers()
class Foo:
    pass

f = Foo()

assert gc.get_referrers(f) == [f.__dict__, f.__class__.__dict__]

# Test gc.get_referents()
class Foo:
    pass

f = Foo()

assert gc.get_referents(f) == [{}, f.__class__.__dict__]

# Test gc.get_objects()
class Foo:
    pass

f = Foo()

assert f in gc.get_objects()
assert gc.get_objects()

# Test gc.get_stats()
assert gc.get_stats()

# Test gc.get_threshold()
assert gc.get_threshold()

# Test gc.set_threshold()
gc.set_th
