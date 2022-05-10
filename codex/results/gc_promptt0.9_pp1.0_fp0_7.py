import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't leave uncollectable objects with the wrong flags

# Test the case where collect() finds only an uncollectable obje
