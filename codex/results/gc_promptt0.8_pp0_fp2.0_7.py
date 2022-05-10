import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on uncollectable objects.

# C doesn't call tp_clear(o) on uncollectable objects.  (Python
# 2.3a3 does.)  If we *do* clear the objects (e.g., by calling
# gc.collect()), then we have to make sure that the objects are
# aware that they've been cleared.  (There are no destructors for
# uncollectable objects.)  Otherwise, we get the error:
# *** AttributeError: 'string' object has no attribute 'x'

# Since we're trying to collect the uncollectable, we need to make
# uncollectable objects collectable in the first place.  That is, we
# need to keep them around until they would normally be collected.
# To do that, we use a weakref callback.  The callback won't be
# called when the object is garbage collected, but will be called
# when it's no longer uncollectable.

def callback(wr, obj=None):
    if obj is None:
        obj = wr()
    obj.x = None

def make_uncollectable
