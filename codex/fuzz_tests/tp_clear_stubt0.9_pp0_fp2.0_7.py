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
del func, cyc, latefin

gc.collect()
</code>
The <code>__del__</code> in <code>LateFin</code> accesses <code>tuple</code>'s <code>__new__</code> from the previous <code>gc</code> collection without maintaining its refcount by subtracting 1 from the <code>__dict__</code> of the <code>func</code> variable in the <code>Cyclic</code> <code>__del__</code>. <code>tuple</code>'s <code>__new__</code> is then collected and the interpreter crashes when <code>LateFin</code>'s <code>__del__</code> tries to create the <code>weakref</code>
It would not be the first (and probably not the last) bug that I've reported that was closed "hard to reproduce" (and probably won't be the last that I report that is eventually fixed)

