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

import sys
print(sys.getrefcount(latefin))
print(latefin.ref())
print(sys.getrefcount(latefin.ref()))
</code>
This program outputs:
<code>2
&lt;function &lt;lambda&gt; at 0x7f2db4e4a0d0&gt;
2
</code>
So, it seems that the <code>LateFin</code> instance is still alive, even though it has no references to it, and that it points to a function instance that is also still alive, even though it has no references to it.
Is this expected behavior?

