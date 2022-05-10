import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to update collection counts
gc.collect()

print(gc.get_count())
print(gc.get_stats())
print(gc.get_objects())
print({id(obj): w for w, obj in weakref.WeakValueDictionary(id, gc.get_objects()).items() if isinstance(obj, int) is False})
