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
print(latefin.ref())
</code>
The output is:
<code>&lt;function &lt;lambda&gt; at 0x7f1c1e8e8f80&gt;
</code>
The <code>LateFin</code> object is destroyed, which should also destroy <code>func</code> but it doesn't.

