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
latefin.__dict__.clear()
del latefin.ref
latefin = None
gc.collect()
</code>
Running <code>python test_weakref_extra.py</code> from the shell will then give:
<code>&lt;bound method ?.&lt;lambda&gt; of None&gt;
</code>
So, not pretty, but it does the trick.
Depending on what you need to do, you might also be interested in eumd.

