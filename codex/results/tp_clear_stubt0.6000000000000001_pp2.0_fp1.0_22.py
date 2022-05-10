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

print(latefin.ref)

"""

# The problem is that the LateFin object is a finalizer, and so is
# the second element of the tuple.  The finalizer for the tuple is
# called first, which replaces the "ref" attribute of the LateFin
# object with a weakref which points to the func object.  Then the
# LateFin finalizer is called, and latefin.ref is a weakref to the
# func object, but the func object has already been collected, so it
# is dead.  So the LateFin finalizer tries to call latefin.ref(), and
# segfaults.

# This is not a problem with the new-style gc.  The old-style gc
# doesn't collect the func object, because there is still a reference
# to it from the LateFin object.  That's a problem in and of itself,
# but it's not a segfault.

# This is also not a problem in the new-style gc when the tuple is a
# subclass of tuple.  In that case, the
