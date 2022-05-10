import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This used to seg fault.
gc.collect()

# Test gc.get_objects().
gc.get_objects()

# This used to seg fault.
gc.collect()

# Test gc.get_referrers().
gc.get_referrers(object())

# This used to seg fault.
gc.collect()

# Test gc.get_referents().
gc.get_referents(object())

# This used to seg fault.
gc.collect()


# Test weakref.ref().

class Foo(object):
    pass

foo = Foo()
a = weakref.ref(foo)

# This used to seg fault.
gc.collect()

del foo

# This used to seg fault.
gc.collect()
