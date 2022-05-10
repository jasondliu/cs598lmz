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

# print(latefin.ref())
# print(latefin.ref()())
print(latefin.ref()())
</code>
I'm getting
<code>&lt;function &lt;lambda&gt; at 0x7f4f88a8a400&gt;
&lt;function &lt;lambda&gt; at 0x7f4f88a8a400&gt;
</code>
but I'm expecting to see <code>&lt;function &lt;lambda&gt; at 0x7f4f88a8a400&gt;</code> and <code>None</code>


A:

I think you might be misunderstanding what the problem is. The problem is that the <code>LateFin</code> instance is not garbage collected. It is not that the function it references is not garbage collected.
The problem is that the <code>LateFin</code> instance is referenced by a <code>weakref</code> object in the <code>Cyclic</code> instance.
This means that the <code>LateFin</code> instance
