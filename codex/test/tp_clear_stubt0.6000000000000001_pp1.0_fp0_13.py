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

# Ensure that the LateFin instance is still alive, and that
# its __del__ method hasn't run yet.
if latefin.ref() is not None:
    assert gc.get_referrers(latefin) == [latefin], gc.get_referrers(latefin)
    assert gc.collect() == 0

# Ensure that the LateFunc instance has been collected, and
# that the reference from the LateFin instance has been cleared.
if gc.collect() == 0:
    assert gc.get_referrers(latefin) == [], gc.get_referrers(latefin)
else:
    # The LateFin instance may not have been cleaned up yet, but
    # its reference must have been cleared.
    assert gc.get_referrers(latefin) == [latefin], gc.get_referrers(latefin)
    assert latefin.ref() is None
