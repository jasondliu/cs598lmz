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
which prints
<code>&lt;function &lt;lambda&gt; at 0x7f14e6e2c6a8&gt;
</code>
This is not a complete solution, because it requires the <code>LateFin</code> instance to be reachable, but it shows that the problem is not that the module is not reachable.

