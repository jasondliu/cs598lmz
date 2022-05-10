import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
x = [1, 2, 3]
x = None
gc.collect()

# Test gc.garbage collection
x = []
x.append(x)
gc.collect()
print gc.garbage[0][0]

# Test gc.get_debug
print gc.get_debug()

# Test gc.get_objects
print 'gc.get_objects() =', len(gc.get_objects())
# Test gc.get_referrers
print len(gc.get_referrers(gc))
print len(gc.get_referrers(gc.garbage))
print len(gc.get_referrers(gc.get_objects))

# Test gc.get_threshold
print gc.get_threshold()

# Test gc.set_debug
# gc.set_debug(gc.DEBUG_LEAK)

# Test gc.set_threshold
gc.set_threshold(10, 10, 10)

# Test gc.get_count
print gc.get_count
