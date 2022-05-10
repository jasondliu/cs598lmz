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
gc.collect()
gc.collect()

print(latefin)
del latefin
gc.collect()
print(func)
</code>
The output is:
<code>&lt;__main__.LateFin object at 0x7f4a6b8e6d68&gt;
&lt;function &lt;lambda&gt; at 0x7f4a6b8e6b70&gt;
</code>
The <code>LateFin.__del__</code> method is called, and <code>LateFin.ref</code> is set to a weak reference to <code>func</code>.  But when <code>LateFin.__del__</code> returns, <code>LateFin.ref</code> is cleared by the garbage collector.  This happens before <code>Cyclic.__del__</code> is called, so <code>Cyclic.__del__</code> gets a reference to a dead object.
The <code>Cyclic.__del__</code>
