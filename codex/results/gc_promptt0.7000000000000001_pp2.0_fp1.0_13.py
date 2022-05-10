import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
#   Create a number of objects and then make them unreachable.  Verify that
#   they are collected.  Also check that the old objects are removed from the
#   old list.

import gc, weakref

class C:
    pass

if __name__ == "__main__":
    objects = [C() for i in range(30)]
    objects += [C() for i in range(30)]
    objects += [C() for i in range(30)]
    objects += [C() for i in range(30)]

    # Keep these objects alive until the end of the test
    keepalive = objects[:]

    refs = [weakref.ref(obj) for obj in objects]

    del objects
    gc.collect()

    for i in range(len(refs)):
        ref = refs[i]
        if ref() is not None:
            print("BUG: unreachable object was not collected")

    # Check to make sure that the unreachable objects at the end of the old
    # list were removed
    old = gc.
