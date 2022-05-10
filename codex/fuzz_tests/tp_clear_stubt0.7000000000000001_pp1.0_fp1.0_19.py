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
This code will cause:
<code>Fatal Python error: Reference cycle not cleaned up
</code>
(I've left the <code>gc.collect()</code> call in there because that's the only way it's possible to reproduce the issue with pypy; without it, no reference cycle is created.)
However, if I change <code>func.__module__ = cyc</code> to <code>func.__module__ = cyc[0]</code> then the code does not crash. (The resulting reference cycle is <code>func -&gt; LateFin -&gt; func</code>; the one created by assigning <code>func.__module__ = cyc</code> is <code>func -&gt; LateFin -&gt; func -&gt; Cyclic -&gt; func</code>.)
There is also a similar crash at line 894 of <code>Objects/typeobject.c</code> when <code>func.__name__</code> is set to <code>cyc</code>.
Is this a bug in CP
