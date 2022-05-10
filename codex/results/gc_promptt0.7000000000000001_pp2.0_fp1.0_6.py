import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable
gc.collectable(weakref.ref(1))
gc.collectable(1)
gc.collectable(weakref.ref(weakref.ref(1)))

# Test gc.get_referrers
gc.get_referrers(1)
gc.get_referrers(weakref.ref(1))
gc.get_referrers(weakref.ref(weakref.ref(1)))

# Test gc.get_referents
gc.get_referents(1)
gc.get_referents(weakref.ref(1))
gc.get_referents(weakref.ref(weakref.ref(1)))

# Test gc.get_threshold
gc.get_threshold()

gc.get_objects()
gc.get_stats()
gc.get_count()

# Test gc.collect
gc.collect()
gc.collect()

gc.set_debug(0)
