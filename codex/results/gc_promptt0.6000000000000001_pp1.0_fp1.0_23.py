import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by creating a large number of objects.
# This should trigger a collection.
for i in range(100):
    x = weakref.WeakValueDictionary()
    x['foo'] = [x]
    x = i

gc.collect()
