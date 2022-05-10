import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass
x = C()
print(gc.collect())
# Test gc.is_tracked()
x = None
print(gc.is_tracked(C))
# Test gc.get_referrers()
print(gc.get_referrers(C))
print(gc.get_referrers(gc))
# Test gc.get_referents()
print(gc.get_referents(gc))
print(gc.get_referents(gc, type(gc)))
# Test gc.get_objects()
print(gc.get_objects())
# Test gc.get_count()
print(gc.get_count())
# Test gc.get_threshold()
print(gc.get_threshold())
# Test gc.set_threshold()
gc.set_threshold(1)
print(gc.get_threshold())
gc.set_threshold(2)
print(gc.get_threshold())
# Test gc.get_debug()
print(gc.get_debug
