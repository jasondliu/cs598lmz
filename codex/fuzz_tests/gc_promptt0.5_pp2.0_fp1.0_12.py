import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.collect())
gc.garbage
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers()
# Test gc.get_referents()
gc.get_referents()
# Test gc.is_tracked()
gc.is_tracked()
# Test gc.set_debug()
gc.set_debug()
# Test gc.set_threshold()
gc.set_threshold()
# Test gc.get_count()
gc.get_count()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.get_debug()
gc.get_debug()
# Test gc.get_stats()
gc.get_stats()
# Test gc.set_refs_debug()
gc.set_refs_debug()
# Test gc.get_refs_debug()
gc.get_refs_debug()
# Test gc.enable
