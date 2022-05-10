import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to be sure that in the presence of weakrefs,
# collectable objects are collected

# This test is necessary to make sure the gc module can properly
# deal with the presence of weakrefs.  Previous to version 1.5,
# gc didn't know how to handle weakrefs, and would crash Python.
# Now, it just ignores weakrefs, and collects the objects they
# refer to.  This should work even when the weakrefs themselves are
# collected, so long as nothing is holding a reference to them.
# This test checks that that is so.
#
# Here, we leak a bunch of weakrefs, then force a collection.
# The leak is detected, and an exception is raised.

def callback(wr):
    print "called back"

def main():
    collected = []
    for i in range(100):
        for j in range(100): # make some objects to collect
            k = []
        wr = weakref.ref(k, callback)
        collected.append(k)
    del collected
    # At this point, there are many objects (
