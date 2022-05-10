import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print 'gc.collect():', gc.collect()
# Test gc.garbage
print 'gc.garbage:', gc.garbage
# Test gc.get_count()
print 'gc.get_count():', gc.get_count()
# Test gc.get_debug()
print 'gc.get_debug():', gc.get_debug()
# Test gc.get_objects()
print 'gc.get_objects():', len(gc.get_objects())
# Test gc.get_referrers()
print 'gc.get_referrers():', len(gc.get_referrers(gc))
# Test gc.get_threshold()
print 'gc.get_threshold():', gc.get_threshold()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
print 'gc.set_threshold():', gc.get_th
