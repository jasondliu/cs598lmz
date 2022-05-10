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
This is a variation of the issue that was first publicized here, where the change from 2.5 to 2.6 put classes into the function's <code>__globals__</code> instead of their <code>__module__</code>.  Some of the same ideas would apply, but the latter is not set, and therefore (at least by default) not cleaned up by the cyclic gc.

