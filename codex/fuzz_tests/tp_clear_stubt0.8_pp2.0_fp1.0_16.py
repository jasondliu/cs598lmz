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

try:
    next(latefin.ref())
except StopIteration:
    pass
</code>
The linked test case only shows that the <code>Cyclic</code> object isn't collected in Python 2.6. I can't get that to happen in 2.6 either, not even if I also remove the <code>__slots__</code> from <code>Cyclic</code>. It does get collected in 2.7 and 3.1, but only if there are other cycles present, so that the reference count of the <code>Cyclic</code> object is reduced.

