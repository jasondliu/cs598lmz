import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# gc.collect()
# print(gc.garbage)
# print(gc.get_count())
# print(gc.get_threshold())
# print(gc.is_tracked(s))
# print(gc.is_tracked(gc.get_referents(s)))
# print(gc.get_referrers(s))
# print(gc.get_objects())
# print(gc.get_stats())
# print(gc.get_referrers(gc.get_objects()[-1]))
def get_object_info(obj):
    print(obj)
    print(gc.is_tracked(obj))
    print(gc.get_referents(obj))
    print(gc.get_referrers(obj))
    print()
# print(gc.get_objects())
# print(gc.get_referents(gc.get_objects()[-1]))
# print(gc.get_referrers(gc.get_objects()[-1]))

# Test weakref
# s
