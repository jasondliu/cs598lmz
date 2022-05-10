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
It creates a <code>LateFin</code> object with a weakref to a function, a <code>Cyclic</code> object that references the <code>LateFin</code> object, and a function that references the <code>Cyclic</code> object. When the <code>Cyclic</code> object is deleted, it sets the weakref to the function in the <code>LateFin</code> object, and deletes the <code>LateFin</code> object.
When I run this, I get <code>None</code> printed.

