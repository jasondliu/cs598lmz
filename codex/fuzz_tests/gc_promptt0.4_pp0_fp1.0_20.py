import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_count()
gc.get_count()
# Test gc.get_stats()
gc.get_stats()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
# Test gc.is_tracked()
gc.is_tracked(10)
gc.is_tracked(None)
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
# Test gc.garbage
gc.garbage
# Test gc.callbacks
def callback(phase, info):
    print phase, info
gc.callbacks.append(callback)
gc.collect()
# Test gc.disable()
gc.disable()
# Test gc.enable()
gc.enable()
# Test gc.isenabled()
gc.isenabled()
# Test gc.get_referrers()
gc.get_referrers(gc)
#
