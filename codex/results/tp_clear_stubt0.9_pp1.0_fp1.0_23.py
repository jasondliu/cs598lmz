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
</code>
As you can see, I forced the cyclic:
<code>&gt;&gt;&gt; gc.collect()
3
&gt;&gt;&gt; gc.garbage
[((&lt;function &lt;lambda&gt; at 0x0275EC30&gt;, &lt;__main__.LateFin object at 0x029D3D70&gt;),)]
</code>

