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
del func, cyc, LateFin, Cyclic
gc.collect()
</code>
The idea is that <code>LateFin.__del__</code> will be called as soon as <code>cyc</code> is collected, and <code>Cyclic.__del__</code> will be called at the very end. A global reference from <code>LateFin</code> to the function will prevent it from being collected, and another global reference from it to <code>Cyclic</code> will prevent the function from being collected. The global reference to <code>Cyclic.__new__</code> will prevent <code>Cyclic</code> from being collected, and the global reference to <code>tuple.__new__</code> will prevent <code>Cyclic.__new__</code> from being collected.
In CPython, <code>func</code> is the only object left in the cycle and the function will be collected soon after the end of the script.

