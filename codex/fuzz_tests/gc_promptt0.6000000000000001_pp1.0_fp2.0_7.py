import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()
# Still no objects collected.
gc.collect()
# Now objects are collected.
gc.collect()
gc.collect()
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still no objects collected.
gc.collect()
# Still
