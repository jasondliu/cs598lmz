import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefable objects
# The idea is to create a weak reference to an object
# and then delete all references to that object.
# Collecting garbage should then call the object's
# tp_clear method, which should clear the weak
# reference and make the object uncollectable.

# By default, collectable objects are not tracked by
# cyclic gc.

def createmany():
    # Create many objects, and create a weak reference to each one.
    # After creating the objects, destroy all references to them,
    # so they become uncollectable.  Then call gc.collect().
    # Afterwards, check that weakref.ref is dead for each object.
    for i in range(10):
        # create 10 objects
        obj = C()
        # create a weak reference to each object
        objref = weakref.ref(obj)
        # clear all references to the object
        del obj
        del objref
    # run garbage collection
    gc.collect()
    # check weakref.ref objects
    # they should now be dead
    for i in range(
