import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect:
weakref.ref(gc.collect())
# Test gc.garbage:
gc.garbage
# Test gc.get_count:
gc.get_count()
# Test gc.get_debug:
gc.get_debug()
# Test gc.get_objects:
gc.get_objects()
# Test gc.get_referrers:
gc.get_referrers(gc)
# Test gc.get_stats:
gc.get_stats()
# Test gc.is_tracked:
gc.is_tracked(gc)
# Test gc.set_debug:
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.set_threshold:
gc.set_threshold(1,1,1)
# Test gc.callbacks:
gc.callbacks

gc.DEBUG_COLLECTABLE
gc.DEBUG_UNCOLLECTABLE
gc.DEBUG_SAVEALL
gc.DEBUG_LEAK
gc.DEBUG_STATS
gc.DEBUG_INSTANCES
gc.DEBUG_OB
