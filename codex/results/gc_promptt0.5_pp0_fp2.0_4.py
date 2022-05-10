import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is mainly used to check that collect() really collects
# cyclic trash.  If it doesn't, the weakrefs will get triggered
# during the test.

class C:
    pass

# Create a cycle
c1 = C()
c2 = C()
c1.x = c2
c2.x = c1

# Create a weakref to c1
wr = weakref.ref(c1)

# Enter the reference in a list, to keep it alive until we clear() the list
L = [wr]

# Clear the local variables, and trigger a collect
c1 = c2 = None
gc.collect()

# Now we can check that the weakref is dead
if wr() is None:
    print "ok"
else:
    print "not ok"
