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
del latefin
gc.collect()

gc.garbage.clear()
gc.garbage.append(func)
del func
gc.collect()

# test that the instance is not resurrected
assert not hasattr(gc.garbage[0], 'ref')

gc.garbage.clear()
gc.garbage.append(func)
del func
gc.collect()

# test that the instance is not resurrected
assert not hasattr(gc.garbage[0], 'ref')
