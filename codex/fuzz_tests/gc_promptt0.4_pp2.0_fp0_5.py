import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print gc.collect()

# Test gc.get_objects()
print len(gc.get_objects())

# Test gc.garbage
print len(gc.garbage)

# Test gc.get_referrers()
print len(gc.get_referrers(gc))

# Test gc.get_referents()
print len(gc.get_referents(gc))

# Test gc.DEBUG_STATS
gc.set_debug(gc.DEBUG_STATS)
print gc.collect()

# Test gc.DEBUG_LEAK
gc.set_debug(gc.DEBUG_LEAK)
print gc.collect()

# Test gc.DEBUG_SAVEALL
gc.set_debug(gc.DEBUG_SAVEALL)
print gc.collect()

# Test gc.DEBUG_UNCOLLECTABLE
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print gc.collect()

# Test gc.DEBUG_INSTANCES
gc.set_debug(gc
