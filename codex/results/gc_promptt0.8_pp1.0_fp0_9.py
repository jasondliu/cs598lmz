import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without the garbage collector.
gc.disable()
# Create gc objects (there should be none)
wkeepalive = weakref.ref(keepalive)
del keepalive
# Call gc.collect()
gc.collect()
# The garbage collector should not have collected the wkeepalive.
print(wkeepalive())
# Call gc.collect()
gc.collect()
# There's nothing to collect, so the garbage collector should do nothing.
print(wkeepalive())
# The garbage collector no longer knows that the object is collectable.
print(gc.is_tracked(wkeepalive()))

# Test gc.collect() with the garbage collector.
# Reenable the garbage collector.
gc.enable()
# Call gc.collect()
gc.collect()
# The garbage collector should still not have collected the wkeepalive,
print(wkeepalive())
# but the garbage collector now knows that the object is collectable.
print(gc.is_tracked(wkeepalive()))
# Call gc.collect()
gc.collect()
