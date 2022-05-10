import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
l = [gc.collect() for i in range(100)]
assert l == [0] * 100
# Test gc.garbage
gc.collect()
gc.garbage.append(42)
gc.collect()
assert gc.garbage == [42]
# Test gc.get_count()
gc.collect()
l = gc.get_count()
assert len(l) == 3
assert min(l) == 0
assert max(l) == sys.getrecursionlimit()
# Test gc.get_debug()
gc.collect()
d = gc.get_debug()
assert d == gc.DEBUG_STATS
# Test gc.get_threshold()
gc.collect()
l = gc.get_threshold()
assert len(l) == 3
assert min(l) == 0
assert max(l) == sys.getrecursionlimit()
# Test gc.set_debug()
gc.collect()
gc.set_debug(gc.DEBUG_STATS)
# Test gc.set_threshold()
gc.
