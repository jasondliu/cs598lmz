import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class A:
    pass

class B:
    def __init__(self, x=None):
        self.x = x

def get_all_objects():

    # Construct a list of all collectable objects, excluding the list itself
    # and modules (for which gc.is_tracked() is False) and types (whose
    # instances are tracked rather than the type objects themselves).
    all_objects = gc.collectable()
    all_objects.remove(all_objects)
    all_objects.remove(gc)
    for i in range(len(all_objects)-1, -1, -1):
        o = all_objects[i]
        if (type(o) is type or
            type(o) is types.ModuleType and not gc.is_tracked(o)):
            del all_objects[i]
    return all_objects

# List all objects and check that no two are the same object.
all_objects = get_all_objects()
seen = {}
for i in range(len(all_objects)):
