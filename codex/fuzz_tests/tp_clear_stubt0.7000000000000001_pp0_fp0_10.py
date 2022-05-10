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
After the first collect, the <code>func</code> is still alive, but the <code>ref</code> attribute of <code>latefin</code> is already a <code>weakref</code> to <code>func</code>.  After the second collect, <code>func</code> is dead, but <code>latefin</code> is still alive.  After the third collect, <code>latefin</code> is dead, and the <code>__del__</code> method is called, but since <code>func</code> is already dead, the <code>ref</code> attribute is <code>None</code>, so the <code>__del__</code> method does nothing.

