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
assert latefin.ref() is latefin
gc.collect() # recycle LateFin
assert latefin.ref() is None
del latefin
gc.collect() # recycle cyclic2
gc.collect() # recycle func

del Cyclic, LateFin
gc.collect()
gc.collect()
gc.collect()
