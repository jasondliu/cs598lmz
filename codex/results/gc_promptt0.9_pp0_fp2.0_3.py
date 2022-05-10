import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
w = weakref.ref(object())
# gc.collect()             # Must exist, in order to trigger the bug
assert w() is None
# End of test
