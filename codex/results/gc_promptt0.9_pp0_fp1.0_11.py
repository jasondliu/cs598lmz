import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect function:
#
# This module makes sure gc.collect() does a full collection, clears all
# containers, and calls tp_clear on all objects.  If any containers are found
# after gc.collect() or a mapped object is found that has a non-NULL address
# in its tp_clear slot, the test fails.

# This function returns all objects reachable from obj.
# Copied from test_support.
def all_objects(obj):
    # Yield all objects reachable from obj
    todo = [id(obj)]
    while todo:
        oid = todo.pop()
        o = oldref(oid)
        yield o
        todo.extend(id(c) for c in gc.get_referents(o))

# This function returns all objects in containers.
# Copied from test_support.
def get_objects_in_containers():
    containers = [gc.garbage]
    containers.extend(gc.get_objects())
    objects = []
    done = {}
    while containers:
        container
