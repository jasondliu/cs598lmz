import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() immediately after a call to gc.collect()
gc.collect()
# Not collectable
gc.collect()
gc.collect()
gc.collect()

# Not collectable
gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
gc.collect()
gc.collect()

gc.collect()
