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
latefin.ref()
</code>
<code>latefin</code> is a <code>LateFin</code> object whose <code>__del__</code> method attempts to set <code>func</code> to the value of <code>self.ref</code>.  However, <code>self.ref</code> is a weak reference to itself, and it is collected before <code>latefin</code>.  Therefore, <code>self.ref</code> is set to <code>None</code> by the collector, which means that when <code>latefin</code> finally gets collected, <code>func</code> is assigned <code>None</code>.
So, although I'm not entirely sure why you might have needed to do this, it is possible.

