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
print hasattr(latefin, 'ref') # This should print False!
</code>
The above program should print <code>False</code>, because <code>LateFin.__del__</code> should be called before the <code>Cyclic</code> object is collected. Since the <code>LateFin</code> object has a <code>weakref</code> pointing to <code>func</code>, the <code>func</code> object should be collected and the <code>LateFin</code> object should be garbage as well. So in the end, the <code>LateFin.__del__</code> method can't be called because the <code>LateFin</code> object is collected.
However, the above program prints <code>True</code>.
This bug causes a problem in one of my libraries, and I already have a workaround for it, but it would be nice if I didn't need it.

