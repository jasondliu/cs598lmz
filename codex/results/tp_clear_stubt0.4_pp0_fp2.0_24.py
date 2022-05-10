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
print(latefin.__module__)
</code>
It's a bit more complicated than the previous one, but still not very complicated.
<code>LateFin</code> is a class with a single slot, <code>ref</code>, which is a weak reference to a function.  The <code>__del__</code> method of <code>LateFin</code> sets <code>func</code> to the target of the weak reference.
<code>Cyclic</code> is a subclass of <code>tuple</code> that has a <code>__del__</code> method that sets <code>latefin.ref</code> to a weak reference to the first element of the tuple.
<code>latefin</code> is an instance of <code>LateFin</code>.
<code>func</code> is a function.
<code>cyc</code> is a <code>Cyclic</code> instance whose first element is <code>func</code> and whose second element is <code>latefin</code>.
<code>func.__module__ =
