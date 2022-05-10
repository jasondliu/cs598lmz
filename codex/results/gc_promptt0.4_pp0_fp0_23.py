import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.

# Create a bunch of objects and cyclic trash, and make sure
# gc.collect() finds it all.

import gc

class C(object):
    pass

def create_cycle():
    o = C()
    o.x = o
    return o

# Create a cycle with a length that is a power of two minus one
# so that the cycle detector will visit every object exactly once.
# This is necessary to ensure that all objects in the cycle are
# found to be part of a cycle.
def create_long_cycle(length):
    objs = [C() for i in range(length)]
    for i in range(length):
        objs[i].x = objs[(i+1) & (length-1)]
    return objs[0]

def create_long_cycle_with_finalizer(length):
    objs = [C() for i in range(length)]
    for i in range(length):
        objs[i].x = objs[(i+1) & (length-
