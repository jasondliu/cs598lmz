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

# Check that the cyclic gc didn't create a reference cycle.
import gc
assert len([x for x in gc.get_objects() if isinstance(x, Cyclic)]) == 0
assert len([x for x in gc.get_objects() if isinstance(x, LateFin)]) == 0
