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

# Create a new cycle, which should trigger the finalizer of the old cycle
cyc = tuple.__new__(Cyclic, (func, latefin))

# This should cause the func to be freed, but not the latefin
del cyc
gc.collect()

# This should cause the latefin to be freed, but not the func
del latefin
gc.collect()

# This should cause the func to be freed
del func
gc.collect()
