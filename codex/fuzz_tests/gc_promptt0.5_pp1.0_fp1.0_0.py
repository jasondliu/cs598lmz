import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Create a bunch of objects, then delete references to them, and
# make sure gc.collect() recovers the memory.
# If it doesn't, or if gc.collect() is not needed to recover the
# memory, the Python process will grow without bound.

import sys

def create_objects(n):
    """Create a bunch of objects."""
    for i in range(n):
        yield [i] * i

def test_gc(n):
    """Create a bunch of objects, then delete references to them, and
    make sure gc.collect() recovers the memory."""
    print("creating %d objects..." % n, end=' ')
    sys.stdout.flush()
    objs = list(create_objects(n))
    print("done")
    print("clearing references...", end=' ')
    sys.stdout.flush()
    del objs
    print("done")
    print("collecting...", end=' ')
    sys.stdout.flush()
    n = gc.collect()
    print("done")

