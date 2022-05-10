import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_LEAK)

# Test gc.set_threshold()
gc.set_threshold(10, 10, 10)
gc.collect()

# Test gc.is_tracked()
gc.is_tracked("string")
gc.is_tracked(1)
gc.is_tracked(1.0)
gc.is_tracked(1j)
gc.is_tracked(gc)
gc.is_tracked(weakref)
gc.is_tracked(weakref.WeakValueDictionary())

# Test gc.is_finalized()
gc.is_finalized("string")
gc.is_
