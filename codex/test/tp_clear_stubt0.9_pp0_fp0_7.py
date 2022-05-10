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
del func, cyc, LateFin
gc.collect()

# This was supposed to either leak func in a weird way, or leak that weakref
# object, but in the end, the weird "ErrUnstowedGc" case that this test
# triggered was never exercised because it matched no common case.  It only
# happens when the cycle GC is itself in the middle of a chain of function
# calls (here involving func()) that want to be freed at some later point,
# due to the fact that the func() chain - an object which shouldn't really
# exist, but does as a consequence of the weird way that it happens to get
# garbage collected - becomes weakref'ed.  So, the func() found itself in the
# middle of a "unstow and free" unordered list of objects to be freed by the
# cycle GC and by the "check for later freeing".  The cycle GC finds these in
# the order that they happen to be in, and happens to free first the weakref,
# and then func().  So, the "stow and free" feeding the "check for later
# freeing" weakref object now points to
