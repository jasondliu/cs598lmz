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

# At this point, `latefin` is not yet finalized.  It is kept alive
# by its refcount, and it in turn keeps `func` alive by the weakref.
# There is a reference cycle [type, latefin] with latefin containing a
# Weakref to func.
#
# When we delete `latefin`, it is put in a dying set, and its refcount
# is decremented to -1.  The refcount of `func` is decremented to 0.
#
# When we collect, the reference cycle is not collected because the
# reference to `func` in the cycle (via the weakref) is not strong.
# This is correct.
#
# The dying set is not cleared, because it contains an object with a
# refcount < 0.  This is correct.
#
# However, the refcount of `func` is not decremented further to -1.
# This is a bug, because `func` has become uncollectable.
#
# The problem is that gc.collect() calls tp_clear() on the `type`

