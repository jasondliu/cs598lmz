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
print latefin.ref()
print func()
</code>
The output is:
<code>&lt;function &lt;lambda&gt; at 0x7f6bfe33a9b0&gt;
None
</code>
The problem is that the <code>__del__</code> of <code>Cyclic</code> is called before the <code>__del__</code> of <code>LateFin</code>.

