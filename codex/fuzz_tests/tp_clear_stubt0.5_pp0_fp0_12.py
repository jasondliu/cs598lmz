import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

# This is a regression test for a bug in the gc module.
# The bug was that the gc module was not properly
# tracking objects that were moved in memory by
# realloc().  This test creates a cyclic trash
# structure that contains a function object, and
# then calls gc.collect().  In the past, this would
# cause a segfault, because the gc module would
# visit a pointer to a function object that had
# been freed and reallocated as a tuple object.

# The bug was fixed in Python 2.2a1 by changing
# the gc module to track all objects in a doubly-
# linked list, instead of tracking only the objects
# that were directly part of a cyclic trash
# structure.  This change made the gc module much
# slower, but it also made the gc module much more
# robust.

# Now, the test above should run to completion
# without crashing.  However, it will print a
# debug message to stderr, because the gc module
# doesn't know how to collect the
