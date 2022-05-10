import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for i in range(10):
    gc.collect()
    print('Collecting %d' % i)
    print('Unreachable objects:', len(gc.garbage))
    print('Remaining Garbage:', gc.garbage)
# Test gc.get_referents()
# gc.get_referents()
# Test gc.get_referrers()
# gc.get_referrers()
# Test gc.get_objects()
# gc.get_objects()
# Test gc.get_threshold()
#gc.get_threshold()
# Test gc.set_threshold()
#gc.set_threshold()

# Test gc.get_debug()
#gc.get_debug()
# Test gc.set_debug()
#gc.set_debug()

# Test gc.callbacks
#gc.callbacks

# Test gc.DEBUG_STATS
#gc.DEBUG_STATS

# Test gc.DEBUG_LEAK
#gc.DEBUG_LE
