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

# make sure that the cyclic GC is not triggered
# by the previous test (which should have run
# the cyclic GC)
gc.collect()

# make sure that the cyclic GC did not crash
# and that it cleaned up the cyclic object
if latefin.ref() is not None:
    raise Exception("cyclic GC did not run")
