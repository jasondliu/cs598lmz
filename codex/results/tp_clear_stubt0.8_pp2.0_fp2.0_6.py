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

The <code>LateFin</code> class has a purpose that I don't understand. Its <code>__del__</code> method stores a weakref to <code>func</code> in an instance-specific data attribute (<code>__slots__</code> prevent it from having an attribute dictionary, so assigning to <code>self.ref</code> assigns to an <code>__dict__</code>-like object) and then deletes the global <code>latefin</code> variable which holds a reference to the <code>LateFin</code> instance. If a GC collection happens after <code>latefin</code> is deleted but before <code>func</code> is deleted, then <code>func</code> will not be deleted immediately, and will instead be scheduled for deletion later (<code>ref</code> is a "finalizer", the class that holds the weakref is a "suitable container" for the finalizer, and the <code>__del__</code> method of the container is not a "releasing function").
The <code>Cyclic</code>
