import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs to uncollectable objects
class C:
    pass
c = C()
w = weakref.ref(c)
del c
# Force c to be uncollectable
gc.collect()
# Force w to be collectable
del w
