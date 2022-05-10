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

# verify that there is a cyclic reference with object in the
# reference chain.
gc.collect()
if latefin.ref is None:
    print("could not reproduce the crash")
    raise SystemExit(1)

# create a second one that is not directly reachable
nocyc = LateFin()

# remove the cyclic reference, keeping the LateFin instance alive.
del latefin
gc.collect()
del cyc

# the LateFin instance should be uncollectable since it's contained
# in the reference chain, but the __del__ method should not be called
# because of a bug fixed in http://bugs.python.org/issue14136
if latefin.ref is not None:
    print("could not reproduce the crash")
    raise SystemExit(2)

# the second LateFin instance should be collected.
if not isinstance(weakref.ref(nocyc)(), gc.DeadObjectError):
    print("could not reproduce the crash")
    raise SystemExit(3)
