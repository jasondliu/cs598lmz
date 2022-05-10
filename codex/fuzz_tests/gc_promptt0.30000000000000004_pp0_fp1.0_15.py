import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.
#
# This test is designed to check whether or not a weakref callback
# can resurrect an object that is in the process of being collected.
#
# The test creates a list of objects that are all weakly referenced.
# The objects are then deleted, and the weakref callback is invoked
# for each object.  The callback attempts to resurrect the object by
# appending it to a list.  If the object can be successfully resurrected
# then it will be found in the list after gc.collect() returns.

import gc, weakref

class C:
    pass

def callback(wr):
    l.append(wr)

l = []
for i in range(10):
    c = C()
    l.append(weakref.ref(c, callback))

del c

gc.collect()

print(len(l) == 10)

# Check that the objects have been collected.
for i in range(10):
    print(l[i]() is None)

# Check that the objects have been resurrected.
gc.collect()
