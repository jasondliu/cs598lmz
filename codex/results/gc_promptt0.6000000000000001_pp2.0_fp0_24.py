import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(gc)
# Test gc.get_referents()
gc.get_referents(gc)
# Test gc.get_count()
gc.get_count()
# Test gc.garbage
gc.garbage
# Test gc.set_threshold()
gc.set_threshold(700,10,10)
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.enable()
gc.enable()
# Test gc.disable()
gc.disable()
# Test gc.isenabled()
gc.isenabled()
# Test gc.callbacks
def callback(x):
    x.append(4)

gc.callbacks.append(callback)
del callback
gc.collect()
# Test gc.DEBUG_STATS
gc.DEBUG_STATS
# Test gc.DEBUG_LEAK
gc.
