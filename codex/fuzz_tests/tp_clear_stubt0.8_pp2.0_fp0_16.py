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
del func, cyc, LateFin

gc.collect()
gc.collect()

def test():
    for _ in range(10):
        # the trick: in each iteration, the collectable objects are
        # different, so each __del__() attribute of the cyclic gc
        # objects must be different.
        func()
