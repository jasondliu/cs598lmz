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

# Now, func is kept alive by the weakref in latefin, but latefin is kept alive
# by the reference from func.  This is a reference cycle, but it is not
# detected by the cycle detector, because latefin is a "late-finalizer" object
# (i.e. it has a __del__ method).  This is a bit of a hack, but it is used to
# keep weakref objects alive until the referent is collected.  The problem is
# that latefin is also part of a cycle, so it will never be collected.
#
# The cycle detector should detect this cycle.

gc.collect()

# Now, the weakref in latefin is dead, so func is also dead.  But latefin is
# still alive, so the __del__ method of Cyclic is never called.  The weakref
# in latefin should be cleared, so that the cycle is broken and latefin can be
# collected.

gc.collect()

# Now, latefin is dead, so the __del__ method of Cyclic is called.  This
#
