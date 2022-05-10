import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
# First make a bunch of stuff to collect
for i in range(10):
    weakref.ref(int("1"*1000))
for i in range(10):
    weakref.ref(str("1"*1000))
for i in range(10):
    weakref.ref(tuple([1]*1000))
for i in range(10):
    weakref.ref({1:1}*1000)
# Now collect it
gc.collect()

# Test gc.get_threshold
gc.get_threshold()

# Test gc.get_count
gc.get_count()

# Test gc.set_threshold
gc.set_threshold()

# Test gc.set_debug
gc.set_debug()

# Test gc.is_tracked
gc.is_tracked(str)

# Test gc.get_objects
gc.get_objects()

# Test gc.get_referrers
gc.get_referrers(str)

# Test gc.get_referents

