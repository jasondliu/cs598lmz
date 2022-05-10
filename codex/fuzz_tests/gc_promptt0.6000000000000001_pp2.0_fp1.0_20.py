import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
# Test gc.get_referrers()
def f():
    a = []
    b = [a]
    c = [a,b]
    return c
f()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_stats()
gc.get_stats()
# Test gc.is_tracked()
gc.is_tracked(1)
gc.is_tracked([])
gc.is_tracked(gc)
# Test gc.is_finalized()
gc.is_finalized(1)
gc.is_finalized([])
gc.is_finalized(gc)
# Test gc.get_count()
gc.get_count()
# Test gc.set_threshold()
gc.set_threshold(5)
gc.set_threshold(5, 5, 5)
# Test gc.get_threshold()
gc.get_threshold()
# Test gc
