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

# There's no way to tell the exact number of objects that will be
# collected, but it should be at least one, and it should be a LateFin.
assert gc.collect() >= 1
assert isinstance(latefin, LateFin)

# Create a new LateFin object to be collected
del latefin
latefin = LateFin()

# Create a new cycle
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

# Make sure the new LateFin is collected, and that the
# LateFin from the previous cycle is not
gc.collect()
assert isinstance(latefin, LateFin)
assert not isinstance(func, LateFin)
