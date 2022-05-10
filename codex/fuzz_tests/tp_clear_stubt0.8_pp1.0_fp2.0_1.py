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

In the line
<code>func.__module__ = cyc
</code>
we make the module of func refer to cyc. This is necessary because we're going to delete cyc and latefin, but we want them to be kept alive.
In the line
<code>del latefin
</code>
we delete the only reference to cyc, but because cyc is the module of func, it's kept alive.
In the line
<code>self[1].ref = weakref.ref(self[0])
</code>
we create a weak reference in latefin (the <code>ref</code> slot of the cyc[1] tuple entry) to the function <code>func</code>, which keeps it alive.
In the line
<code>del latefin
</code>
we delete the only remaining reference to cyclic, so it is finalized and the <code>__del__</code> method of cyclic is called, which creates a weak reference to <code>func</code> in latefin and deletes latefin. The only reference to cyclic is
