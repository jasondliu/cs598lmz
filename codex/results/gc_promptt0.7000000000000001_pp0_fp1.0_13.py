import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
class A:
    pass
A = A()
B = A
A.x = A
B.y = A
del A
del B
gc.collect()
gc.set_debug(0)
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
class A:
    pass
A = A()
B = A
A.x = A
B.y = A
del A
del B
gc.collect()
gc.set_debug(0)

###############################################################################
# Test gc.get_debug()

# Test gc.get_debug()
gc.get_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.get_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.get_debug()
gc.set_debug(gc.DEBUG_INSTANCES)
gc.get_debug()
gc.set_debug(gc.DEBUG_OBJECTS)
gc.
