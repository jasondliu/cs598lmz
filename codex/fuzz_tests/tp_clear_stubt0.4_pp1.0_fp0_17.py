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
gc.collect()
gc.collect()
</code>
The code is a bit convoluted, but it's not too hard to understand.  The idea is to create a cycle <code>cyc</code> between a function <code>func</code> and a <code>LateFin</code> instance <code>latefin</code>.  Then, when <code>cyc</code> is collected, it has a <code>__del__</code> method that sets <code>latefin.ref</code> to a weak reference to <code>func</code>.  Then, when <code>latefin</code> is collected, it has a <code>__del__</code> method that sets <code>func</code> to the result of dereferencing <code>latefin.ref</code>.  So, <code>func</code> is only set to the result of dereferencing <code>latefin.ref</code> after <code>latefin</code> has been collected.
The problem is that the <code>__del__</code> method of <code>cy
