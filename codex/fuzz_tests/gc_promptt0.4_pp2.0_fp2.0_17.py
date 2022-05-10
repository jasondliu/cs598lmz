import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_count()
gc.get_count()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()

# Test gc.get_objects()
len(gc.get_objects())

# Test gc.get_referrers()
len(gc.get_referrers(gc))

# Test gc.get_referents()
len(gc.get_referents(gc))

# Test weakref.ref()
r = weakref.ref(gc)
r() is gc
del gc
r() is None

# Test weakref.proxy()
p = weakref.proxy(gc)
p is gc
del gc
try:
    p is gc
except ReferenceError:
    pass

# Test weakref.getweakrefcount()
weakref.getweakrefcount(gc)

#
