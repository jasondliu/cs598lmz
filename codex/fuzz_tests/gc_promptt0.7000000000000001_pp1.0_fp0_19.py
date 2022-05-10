import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect:
#
# - collect()
# - collect(generation)
# - collect(generation, n)
# - collect(generation, n, delay)

# Test gc.garbage

# Test gc.DEBUG_STATS
#
# - print out gc stats

# Test gc.DEBUG_OBJECTS
#
# - print out gc objects

# Test gc.set_debug
#
# - try invalid codes

# Test gc.set_threshold
#
# - try invalid codes

# Test gc.get_objects
#
# - make sure it gets cyclic objects

# Test gc.get_referrers

# Test gc.get_referents

# Test gc.is_tracked

# Test gc.get_count

# Test gc.get_stats

# Test id(x) == id(gc.garbage[n])

# Test gc.is_finalized

# Test weakrefs
#
# - Test callback list
# - Test object finalization (__
