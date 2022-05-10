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
</code>
This shows that the <code>LateFin</code> object is not deleted until the <code>Cyclic</code> object is deleted, which happens after the <code>LateFin</code> object is deleted.
But it's not clear how this is relevant to the original question.

