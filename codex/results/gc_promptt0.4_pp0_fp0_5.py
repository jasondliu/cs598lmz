import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.get_objects()
objs = gc.get_objects()
len(objs)

# Test gc.get_referrers()
refs = gc.get_referrers(*objs)
len(refs)

# Test gc.get_referents()
refs = gc.get_referents(*objs)
len(refs)

# Test gc.get_stats()
gc.get_stats()

# Test gc.is_tracked()
gc.is_tracked(objs[0])

# Test gc.is_finalized()
gc.is_finalized(objs[0])

# Test gc.garbage
gc.garbage

# Test gc.get_count()
gc.get_count()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(700
