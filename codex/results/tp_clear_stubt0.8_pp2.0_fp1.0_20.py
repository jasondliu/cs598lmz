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

# Make sure the weakref callback from the cyclic garbage gets fired
# before the finalizer from the weakref.
del latefin
gc.collect()

# The function is dead, but the module should still be alive for
# the weakref callback to run.
if globals()['func'].__module__ != 1:
    raise RuntimeError("function's module not kept alive by weakref")
