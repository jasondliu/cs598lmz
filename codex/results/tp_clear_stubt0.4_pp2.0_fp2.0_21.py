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
</code>
This code will cause a crash in the <code>__del__</code> method of <code>LateFin</code> because a <code>func</code> object is still reachable, but the <code>__del__</code> method of <code>Cyclic</code> is not called.

