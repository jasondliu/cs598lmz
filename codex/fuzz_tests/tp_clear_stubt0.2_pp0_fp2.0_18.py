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
This prints <code>None</code> on CPython 3.6.1, but <code>&lt;function &lt;lambda&gt; at 0x7f8b8a3b3d08&gt;</code> on PyPy 5.8.0.

