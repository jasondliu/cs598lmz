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

print(latefin)
print(latefin.ref())
print(latefin.ref().__module__)
</code>
This prints:
<code>&lt;__main__.LateFin object at 0x00000000026A9B48&gt;
&lt;function &lt;lambda&gt; at 0x00000000026A9C38&gt;
&lt;__main__.Cyclic object at 0x00000000026A9B48&gt;
</code>
So the <code>LateFin</code> object is still alive, and so is the <code>Cyclic</code> object, which is the <code>__module__</code> attribute of the <code>func</code> object.

