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

print(latefin.ref())
</code>
The idea is that the <code>LateFin</code> object has a weak reference to the <code>Cyclic</code> object. When the <code>Cyclic</code> object is deleted, it replaces the weak reference with a strong reference, so the <code>LateFin</code> object is not deleted.
The <code>Cyclic</code> object is created with a reference to a function. When the function is deleted, it is replaced with a reference to the <code>Cyclic</code> object, causing a cycle.
The <code>LateFin</code> object is created with a reference to the function. When the function is deleted, it is replaced with a reference to the <code>Cyclic</code> object, so the <code>LateFin</code> object is not deleted.

