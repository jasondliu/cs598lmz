import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
w = weakref.ref(object())
# w is alive
gc.collect()
# w is dead

# Test gc.get_threshold()
gc.get_threshold()
# (700, 10, 10)

# Test gc.get_count()
gc.get_count()
# (0, 0, 0)
gc.collect()
gc.get_count()
# (0, 0, 0)

# Test gc.set_threshold()
gc.set_threshold(100, 10, 10)
gc.get_threshold()
# (100, 10, 10)

# Test gc.get_objects()
gc.get_objects()
# [<frame object at 0x7f80e7d9b0f8>, <frame object at 0x7f80e7d9b0f8>,
#  <frame object at 0x7f80e7d9b0f8>, <frame object at 0x7f80e7d9b0f8>,
#  <frame object at 0x7f80e
