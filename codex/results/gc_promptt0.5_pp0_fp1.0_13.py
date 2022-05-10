import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
#
# This script creates a bunch of objects, some of which are tracked by
# weakrefs.  gc.collect() is called repeatedly, and we make sure the right
# objects go away at the right time.
#
# The objects are arranged in a cycle, to make sure the cyclic garbage
# collector does the right thing.
#
# This test is a bit tricky, because we have to wait for a certain number
# of collections to occur.  The basic strategy is to create a bunch of
# objects, then collect repeatedly until a certain number of objects are
# known to have been collected.

import gc, weakref

# Create a bunch of objects, and record the set of all objects we create.

all = set()

class C:
    pass

for i in range(10):
    c = C()
    all.add(c)
    c.x = C()
    all.add(c.x)

# Create a cycle, to make sure the cyclic garbage collector is doing its
# job.  Note that we have to be careful to break
