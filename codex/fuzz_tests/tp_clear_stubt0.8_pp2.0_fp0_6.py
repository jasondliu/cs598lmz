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

print gc.collect()
print latefin.ref()
</code>
Output:
<code>0
&lt;function &lt;lambda&gt; at 0x00D6C8E0&gt;
</code>
I don't expect there's a good way to get rid of the memory leak (I can imagine useless use-cases for this leak), but I thought it was interesting and there might have been a good way to do it in py3k.

