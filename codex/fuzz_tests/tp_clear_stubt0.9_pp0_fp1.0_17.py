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
# the __del__ of Cyclic will be forced to finish before the __del__ of LateFin, because the
# weakref would be dead before the __del__ of LateFin.

print(func())
</code>
Without the __module__ = cyc, the output is:
<code>Trying to print a weakly dead object
</code>
With the __module__ = cyc, the output is:
<code>&lt;function at 0x7f7de98d3f90&gt;
</code>

