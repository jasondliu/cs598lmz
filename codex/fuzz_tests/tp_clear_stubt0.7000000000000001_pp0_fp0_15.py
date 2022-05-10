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
del func, cyc, latefin
gc.collect()
</code>
The output of this is:
<code>&lt;function Cyclic.__new__.&lt;locals&gt;.&lt;lambda&gt; at 0x563b1931b7b8&gt;
</code>
I'm not sure why this is happening, it seems like a bug to me.

