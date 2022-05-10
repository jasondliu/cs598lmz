import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations(*tuple, **kwargs)
assert not gc.collect_generations()
# Test gc.get_referrers(*tuple)
assert sys.getrefcount(object()) == 2
l = [object(), object()]
assert sys.getrefcount(l) == 2
assert object() in gc.get_referrers(l)
# Test gc.get_referents(*tuple)
assert list(map(sys.getrefcount, gc.get_referents(l))) == [1, 1]
# Test gc.get_threshold()
assert gc.get_threshold() == (700, 10, 10)
# Test gc.get_thresholds()
assert gc.get_threshold() == (700, 10, 10)
# Test gc.get_stats()
assert isinstance(gc.get_stats(), list)
# Test gc.is_tracked()
assert not gc.is_tracked(l)
l.append(l)
assert gc.is_tracked(l)
