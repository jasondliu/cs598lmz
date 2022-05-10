import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
gc.collect()
print(gc.garbage)
gc.garbage = []
gc.collect()
print(gc.garbage)

# Test gc.get_debug() and gc.set_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print(gc.get_debug())
gc.set_debug(gc.DEBUG_COLLECTABLE)
print(gc.get_debug())

# Test gc.get_count()
print(gc.get_count())

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.get_referrers()
print(gc.get_referrers())

# Test gc.get_stats()
print(gc.get_stats())

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.is_tracked()
class Foo:
    pass

a = Foo()
print(gc.is_tracked(a))

# Test
