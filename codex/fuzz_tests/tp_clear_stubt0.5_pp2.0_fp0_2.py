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

latefin.__module__
del latefin
gc.collect()

# this should not crash
gc.garbage[0]()

# and this should not crash, either
gc.garbage.append(gc.garbage[0])
del gc.garbage[0]
gc.collect()
