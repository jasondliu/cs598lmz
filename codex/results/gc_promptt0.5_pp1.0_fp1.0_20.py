import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.
# This tests the main feature of the collect module.
#
# Create a bunch of objects, and a bunch of weak references to them.
# Explicitly break cyclic references.  Then call gc.collect(), and
# check that the objects have been deleted.
#
# This test is primarily intended to check that collect() is working
# at all.  It doesn't check that collect() is doing anything useful.
# In particular, it doesn't check that collect() collects cycles.
# (The tests in test_gc.py check that.)

import gc, weakref

# Create a bunch of objects.
# The objects are arranged in a cycle, so they can't be collected
# individually.

class A:
    pass

a = A()
a.a = a

b = A()
b.b = b

a.b = b
b.a = a

# Create a bunch of weak references to the objects.

wa = weakref.ref(a)
wb = weakref.ref(b)

# Break the cycle, so the objects are
